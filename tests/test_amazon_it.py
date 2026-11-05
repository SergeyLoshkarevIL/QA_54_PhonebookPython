import time

from pages.pages_amazon_it import AmazonIt


class TestAmazonIt:
    def test_auth_amazon(self, driver):
        email = "kristitomash@gmail.com"
        password = "0534711279Kris!"
        pages_amazon = AmazonIt(driver,"https://www.amazon.it")
        pages_amazon.open()
        pages_amazon.login(email,password)
        assert "Ciao Kristina" == pages_amazon.get_login()


        time.sleep(20)