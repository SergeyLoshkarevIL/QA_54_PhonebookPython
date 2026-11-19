from faker import Faker
from models.contact import Contact
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage

fake = Faker()
def create_contact():
    return Contact(
        name =fake.first_name(),
        last_name=fake.last_name(),
        phone=fake.numerify("05########"),
        email =fake.email(),
        address = fake.street_address(),
        description= fake.sentence(nb_words=2)
    )


def test_edit_contact_name_field(authenticated):
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_name = fake.first_name()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_mode(contacts_page.EDIT_NAME_INPUT, new_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_name_for_phone(contact) == new_name


def test_edit_contact_last_name_field(authenticated):
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_last_name = fake.last_name()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_mode(contacts_page.EDIT_LAST_NAME_INPUT, new_last_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_last_name(new_last_name) == new_last_name


def test_edit_contact_phone_field(authenticated):
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_phone = fake.numerify(text = "05########")

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_mode(contacts_page.EDIT_PHONE_INPUT, new_phone)
    contacts_page.submit_edit()

    assert contacts_page.contact_cards_visible(new_phone)

def test_edit_contact_email_field(authenticated):
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_email = fake.email()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_mode(contacts_page.EDIT_EMAIL_INPUT, new_email)
    contacts_page.submit_edit()

    assert contacts_page.contact_email() == new_email