from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage

class ContactPage(BasePage):
    ADD_CONTACT_BUTTON = (By.CSS_SELECTOR, "[href='/add']")
    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='description']")
    SAVE_BUTTON = (By.XPATH, "//button[contains(., 'Save')]")

    def open_contact_form(self):
        self.click(self.ADD_CONTACT_BUTTON)

    def fill_name(self,name):
        self.fill(self.NAME_INPUT, name)

    def fill_last_name(self,last_name):
        self.fill(self.LAST_NAME_INPUT, last_name)

    def fill_phone(self,phone):
        self.fill(self.PHONE_INPUT, phone)

    def fill_email(self,email):
        self.fill(self.EMAIL_INPUT, email)

    def fill_address(self,address):
        self.fill(self.ADDRESS_INPUT, address)

    def fill_description(self,description):
        self.fill(self.DESCRIPTION_INPUT, description)

    def fill_contact(self,contact):
        self.fill_name(contact.name)
        self.fill_last_name(contact.last_name)
        self.fill_phone(contact.phone)
        self.fill_email(contact.email)
        self.fill_address(contact.address)
        self.fill_description(contact.description)

    def submit_contact(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def contact_card_visible(self, phone):
        locator = (By.XPATH, f"//h3[contains(text(),'{phone}')]")
        element = WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(locator))
        return element.is_displayed()

    def open_contact_details_card(self, phone):
        card = self.driver.find_element(By.XPATH, f"//h3[contains(text(),'{phone}')]/..").click()