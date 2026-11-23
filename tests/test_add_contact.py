import random
from faker import Faker

from models.contact import Contact
from pages.add_contact_page import ContactPage

fake = Faker()


def test_add_contact_success(authenticated):
    contact_page = ContactPage(authenticated)
    random_suffix = random.randint(1, 99999)
    contact = Contact(
        name = fake.first_name(),
        last_name = fake.last_name(),
        phone=f"05435{random_suffix}",
        email = fake.email(),
        address = fake.street_address(),
        description = fake.sentence(nb_words=4)
        )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)

def test_add_contact_success_all_req_fields(authenticated):
    contact_page = ContactPage(authenticated)
    random_suffix = random.randint(1, 99999)
    contact = Contact(
        name = fake.first_name(),
        last_name = fake.last_name(),
        phone = f"05435{random_suffix}",
        email = fake.email(),
        address = fake.street_address(),
        description= ""
        )

    # contact_page.open_contact_form()
    # contact_page.fill_contact_form(contact)
    # contact_page.submit_contact()
    contact_page.create_contact_steps(contact)

    assert contact_page.contact_card_visible(contact.phone)