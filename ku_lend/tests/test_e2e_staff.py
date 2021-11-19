"""Testing using selenium"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

class SeleniumStaffTests(LiveServerTestCase):
    """Test the staff button and admin page."""

    def setUp(self):
        """Set up for testing."""
        self.browser = webdriver.Chrome('/Users/whachanunya/Downloads/chromedriver')
        url = "https://kulend.herokuapp.com"
        self.browser.get(url)

    def tearDown(self):
        self.browser.quit()

    def test_staff_link(self):
        """Test if the staff button link to correct link."""
        url_list = []
        self.url = self.browser.find_elements_by_tag_name("a")
        for url in self.url:
            page_url = url.get_attribute('href')
            url_list.append(page_url)
        self.assertIn("https://kulend.herokuapp.com/admin/", url_list)
