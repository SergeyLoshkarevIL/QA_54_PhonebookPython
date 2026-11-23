import time

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class ContactsPage(BasePage):
    CONTACTS_LINK = (By.CSS_SELECTOR, "a[href='/contacts']")
    CONTACTS_CARDS = (By.CLASS_NAME, "contact-item_card__2SOIM")
    BUTTON_EDIT = (By.XPATH, "//button[text()='Edit']")
    EDIT_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EDIT_LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    EDIT_PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EDIT_EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    EDIT_ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    EDIT_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='desc']")
    EDIT_SAVE_BUTTON = (By.XPATH, "//button[text()='Save']")
    DETAILS_CARD = (By.CLASS_NAME, 'contact-item-detailed_card__50dTS')
    BUTTON_REMOVE = (By.XPATH, "//button[text()='Remove']")

    def open_contacts_list(self):
        self.click(self.CONTACTS_LINK)
        WebDriverWait(self.driver, 10).until(EC.url_contains("/contacts"))
        time.sleep(1)

    def get_contact_cards_number(self):
        return len(self.driver.find_elements(*self.CONTACTS_CARDS))

    def get_contact_cards(self, phone):
        return self.driver.find_elements(By.XPATH, f"//h3[text()='{phone}']")

    def contact_cards_visible(self, phone):
        locator = (By.XPATH, f"//h3[text()='{phone}']")
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        return element.is_displayed()

    def open_contact_details_card(self, phone):
        self.click(self.get_card_locator(phone))

    @staticmethod
    def get_card_locator(phone):
        return By.XPATH, f"//h3[contains(text(),'{phone}')]"

    def open_edit_mode(self):
        self.click(self.BUTTON_EDIT)

    def set_edit_mode(self, locator, value):
        self.fill(locator, value)

    def submit_edit(self):
        self.click(self.EDIT_SAVE_BUTTON)
        time.sleep(1)

    def contact_name_for_phone(self, phone):
        card = self.find((By.CSS_SELECTOR, ".contact-item-detailed_card__50dTS h2"))
        return card.text.split()[0]

    def contact_last_name(self):
        card = self.find((By.CSS_SELECTOR, ".contact-item-detailed_card__50dTS h2"))
        return card.text.split()[1]

    def contact_email(self):
        card = self.find(self.DETAILS_CARD)
        return card.text.split()[3]

    def remove_current_contact(self):
        logger.info(f"Removing current contact")
        self.click(self.BUTTON_REMOVE)
        time.sleep(1)

    def open_first_contact(self):
        cards = self.driver.find_elements(*self.CONTACTS_CARDS)
        first_card = cards[0]
        first_card.click()

    def remove_all_contacts(self):
        while self.get_contact_cards_number() > 0:
            self.open_first_contact()
            self.remove_current_contact()

