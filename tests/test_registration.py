import pages.registration_page

VALID_EMAIL = "manuel@gmail.com"
VALID_PASSWORD = "Manuel12345$"
INVALID_EMAIL = "manuelgmail.com"
INVALID_PASSWORD = "Manuel12345"

def test_valid_login_success(driver):
    registration_page = pages.registration_page.RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.click_on_registration_button()

    assert registration_page.is_sign_out_displayed()