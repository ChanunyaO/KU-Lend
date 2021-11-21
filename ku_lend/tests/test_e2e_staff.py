# """Testing using selenium"""
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from django.test import LiveServerTestCase
# import os


# class SeleniumStaffTests(LiveServerTestCase):
#     """Test the staff button and admin page."""

#     def setUp(self):
#         """Set up for testing."""
#         self.browser = webdriver.Chrome('/Users/whachanunya/Desktop/KU-Lend/chromedriver')
#         url = "http://127.0.0.1:8000/"
#         self.browser.get(url)

#     def tearDown(self):
#         self.browser.quit()

#     def test_staff_link(self):
#         """Test if the staff button link to correct link."""
#         url_list = []
#         self.url = self.browser.find_elements_by_tag_name("a")
#         for url in self.url:
#             page_url = url.get_attribute('href')
#             url_list.append(page_url)
#         self.assertIn("http://127.0.0.1:8000/admin/", url_list)

#     def test_get_admin_site(self):
#         """Test can get into admin site which check by the user name."""
#         self.browser.find_elements_by_tag_name("a")[1].click()
#         self.browser.find_element_by_id("id_username").send_keys("admin1")
#         self.browser.find_element_by_id("id_password").send_keys("123")
#         self.browser.find_element_by_id("id_password").send_keys(Keys.RETURN)
#         self.user_name = self.browser.find_element_by_id("user-tools").text
#         self.assertIn("ADMIN1", self.user_name)

#     def test_can_click_add_item_page(self):
#         """Test can get into the add item web page."""
#         self.browser.find_elements_by_tag_name("a")[1].click()
#         self.browser.find_element_by_id("id_username").send_keys("admin1")
#         self.browser.find_element_by_id("id_password").send_keys("123")
#         self.browser.find_element_by_id("id_password").send_keys(Keys.RETURN)
#         self.page = self.browser.find_elements_by_class_name("addlink")
#         self.page_url = self.page[4].get_attribute('href')
#         self.assertEqual(self.page_url, "http://127.0.0.1:8000/admin/ku_lend/item/add/")
    
#     def test_add_item(self):
#         """Test if add item success."""
#         self.browser.find_element_by_id("id_username").send_keys("admin1")
#         self.browser.find_element_by_id("id_password").send_keys("123")
#         self.browser.find_element_by_id("id_password").send_keys(Keys.RETURN)
#         self.browser.find_elements_by_class_name("addlink")[4].click()
#         self.browser.find_element_by_id("id_item_name").send_keys("IPad")
#         self.browser.find_element_by_id("id_pickup_place").send_keys("Computer Department")
#         self.browser.find_element_by_id("id_owner").send_keys("Aj.Anan")
#         self.browser.find_element_by_id("id_note").send_keys("-")
#         self.browser.find_element_by_id("id_pub_date_0").send_keys("2021-11-09")
#         self.browser.find_element_by_id("id_pub_date_1").send_keys("08:49:19")
#         self.browser.find_element_by_id("id_item_image").send_keys(os.getcwd()+"/image.png")
#         self.browser.find_element_by_id("id_rate_fee").send_keys("1")
#         self.browser.find_element_by_id("id_max_item_each_user").send_keys("1")
#         self.browser.find_element_by_id("id_max_day_each_user").send_keys("7")
#         self.browser.find_element_by_id("id_max_day_each_user").send_keys(Keys.RETURN)
        
#         self.success_text = self.browser.find_element_by_class_name("success").text
#         self.assertIn('successfully', self.success_text)
