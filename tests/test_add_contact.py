import random

from models.contact import Contact
from pages.add_contact_page import ContactPage


def test_add_contact_success(authenticated):
    contact_page = ContactPage(authenticated)
    random_suffix = random.randint(1, 99999)
    contact = Contact(
        "Kristina",
        "Test",
        f"05435{random_suffix}",
        f"test{random_suffix}@gmail.com",
        "telaviv",
        "qa",
        )

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)

def test_add_contact_success_all_req_fields(authenticated):
    contact_page = ContactPage(authenticated)
    random_suffix = random.randint(1, 99999)
    contact = Contact(
        "Kristina",
        "Test",
        f"05435{random_suffix}",
        f"test{random_suffix}@gmail.com",
        "telaviv",
        ""
        )

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)