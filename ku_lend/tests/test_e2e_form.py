"""Test form using selenium."""
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class FormTest(LiveServerTestCase):
    """Test access profile using selenium."""

    def setUp(self):
        """Set up the parameters for testing."""
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        url = "http://127.0.0.1:8000/"
        self.driver.get(url)

    def test_link_in_form(self):
        """Test that profile button not show if user are not login."""
        index_url = []
        all_tag_a = self.driver.find_elements_by_tag_name("a")
        for link in all_tag_a:
            page_url = link.get_attribute('href')
            index_url.append(page_url)
        find_link = "http://127.0.0.1:8000/profile" in index_url
        self.assertFalse(find_link)

    def test_profile_button_show_after_login(self):
        """Test profile button show when user login."""
        self.driver.find_element_by_xpath("//a[contains(.,'ADMIN')]").click()
        self.driver.find_element_by_name("username").send_keys('admin')
        self.driver.find_element_by_name("password").send_keys('123')
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath("//a[contains(.,'View site')]").click()
        find_profile_button = self.driver.find_element_by_xpath("//a[contains(.,'PROFILE')]")
        assert 'http://127.0.0.1:8000/profile' in find_profile_button.get_attribute("href")
