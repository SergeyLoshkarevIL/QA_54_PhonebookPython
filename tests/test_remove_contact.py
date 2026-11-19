from pages.contacts_page import ContactsPage


def test_remove_contact(authenticated):
    contacts_page = ContactsPage(authenticated)

    contacts_page.open_contacts_list()
    count_before = contacts_page.get_contact_cards_number()
    contacts_page.open_first_contact()
    contacts_page.remove_current_contact()
    count_after = contacts_page.get_contact_cards_number()

    assert count_after == count_before - 1

def test_remove_all_contacts(authenticated):
    contacts_page = ContactsPage(authenticated)

    contacts_page.open_contacts_list()
    contacts_page.remove_all_contacts()

    assert contacts_page.get_contact_cards_number() == 0