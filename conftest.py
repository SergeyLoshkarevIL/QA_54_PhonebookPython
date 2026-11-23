import pytest
from selenium import webdriver
import pages.login_page
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage
from tests.test_edit_contact import create_contact
from tests.test_login import VALID_EMAIL, VALID_PASSWORD
import logging
from utils.logger_config import configure_logger

configure_logger()
logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    logger.info("start browser")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://telranedu.pages.dev")

    yield driver
    logger.info("end browser")

    driver.quit()


@pytest.fixture
def authenticated(driver):
    login_page = pages.login_page.LoginPage(driver)
    login_page.open_login_page()
    login_page.fill_email_field(VALID_EMAIL)
    login_page.fill_password_field(VALID_PASSWORD)
    login_page.click_on_login_button()

    return driver


@pytest.fixture
def ensure_min_contacts(authenticated):
    contacts_page = ContactsPage(authenticated)
    contact_page = ContactPage(authenticated)

    contacts_page.open_contacts_list()
    while contacts_page.get_contact_cards_number()<1:
        contact_page.create_contact_steps(create_contact())
        contacts_page.open_contacts_list()
    return authenticated