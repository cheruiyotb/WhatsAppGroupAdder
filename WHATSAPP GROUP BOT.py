from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import tkinter as tk

class WhatsAppGroupAdder:

    def __init__(self, group_name):
        self.group_name = group_name

        # Set up the WebDriver and navigate to the web WhatsApp page
        self.driver = webdriver.Chrome()
        self.driver.get('https://web.whatsapp.com')

        # Wait for the user to scan the QR code
        input("Scan the QR code, then press Enter to continue...")

        # Find the search box and enter the name of the group you want to add members to
        search_box = self.driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.send_keys(self.group_name)
        search_box.send_keys(Keys.ENTER)

        # Wait for the group page to load
        time.sleep(5)

    def add_number(self, number):
        # Find the "Add Participants" button and click it
        add_participants_button = self.driver.find_element_by_xpath('//div[@title="Add participants"]')
        add_participants_button.click()

        # Wait for the "Add participants" dialog to appear
        time.sleep(3)

        # Find the input box for phone numbers and enter the number
        input_box = self.driver.find_element_by_xpath('//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"]')
        input_box.send_keys(number + Keys.ENTER)

        # Click the "Add" button to add the member
        add_button = self.driver.find_element_by_xpath('//div[@class="_2gOx_ _1fk70 _2H40A"]')
        add_button.click()

        # Wait for the member to be added
        time.sleep(3)

    def close(self):
        # Close the browser
        self.driver.quit()


class WhatsAppGroupAdderGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WhatsApp Group Adder")
        self.root.geometry("300x200")

        # Create input fields for group name and phone number
        group_label = tk.Label(self.root, text="Group Name")
        group_label.pack()
        self.group_entry = tk.Entry(self.root)
        self.group_entry.pack()

        number_label = tk.Label(self.root, text="Phone Number")
        number_label.pack()
        self.number_entry = tk.Entry(self.root)
        self.number_entry.pack()

        # Create button to add a new member
        add_button = tk.Button(self.root, text="Add Member", command=self.add_member)
        add_button.pack()

        # Create button to close the app
        close_button = tk.Button(self.root, text="Close", command=self.close)
        close_button.pack()

        self.adder = None

    def add_member(self):
        # Get the group name and phone number from the input fields
        group_name = self.group_entry.get()
        number = self.number_entry.get()

        # Initialize the WhatsAppGroupAdder instance if it hasn't been initialized yet
        if not self.adder:
            self.adder = WhatsAppGroupAdder(group_name)

        # Add the new member
        self.adder.add_number(number)

    def close(self):
        # Close the WhatsAppGroupAdder instance and exit the app
        if self.adder:
            self.adder.close()
        self.root.destroy
