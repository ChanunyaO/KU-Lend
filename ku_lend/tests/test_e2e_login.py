"""Test using selenium."""
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginTest(LiveServerTestCase):
    """Test access profile using selenium."""

    def setUp(self):
        """Set up the parameters for testing."""
        self.driver = webdriver.Chrome('/Users/premkul/Documents/isp/KU-Lend/chromedriver-3')
        url = "http://127.0.0.1.8000/"
        self.driver.get(url)

    def test_login_link(self):
        """Test if the staff button link to correct link."""
        url_list = []
        self.url = self.driver.find_elements_by_tag_name("a")
        for url in self.url:
            page_url = url.get_attribute('href')
            url_list.append(page_url)
        self.assertIn("http://127.0.0.1.8000/accounts/google/login/", url_list)

    def test_logout_button_show_after_login(self):
        """Test profile button show when user login."""
        self.driver.find_elements_by_tag_name("a")[1].click()
        self.driver.find_element_by_id("id_username").send_keys("admin1")
        self.driver.find_element_by_id("id_password").send_keys("123")
        self.driver.find_element_by_id("id_password").send_keys(Keys.RETURN)
        find_logout_button = self.driver.find_element_by_xpath("//a[contains(.,'LOGOUT')]")
        assert 'http://127.0.0.1:8000/' in find_logout_button.get_attribute("href")
