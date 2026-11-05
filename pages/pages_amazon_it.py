from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AmazonIt:
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def login(self,username,password):
        self.driver.find_element(By.ID,"nav-link-accountList-nav-line-1").click()
        self.driver.find_element(By.ID,"ap_email_login").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
        self.driver.find_element(By.ID,"ap_password").send_keys(password)
        self.driver.find_element(By.ID,"signInSubmit").click()

    def is_logged_in(self, first_name):
        try:
            element = WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.ID, "nav-link-accountList-nav-line-1")))

            return element.text.find(first_name) != -1
        except TimeoutException:
            return False