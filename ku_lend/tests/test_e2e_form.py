# """Test using selenium."""
# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from django.http import HttpResponse, response
# from django.urls import reverse
# import time
#
#
# class FormTest(LiveServerTestCase):
#     """Test access profile using selenium."""
#
#     def setUp(self):
#         """Set up the parameters for testing."""
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option('excludeSwitches', ['enable-logging'])
#         options.add_argument('--headless')
#         self.driver = webdriver.Chrome('/Users/pattananprarom/Downloads/chromedriver')
#         url = "http://127.0.0.1:8000"
#         self.can_click = False
#         self.driver.get(url)
#
#     def test_borrow_amount_input(self):
#         """Test can get into form which check by the user name."""
#         self.driver.find_element_by_xpath("//a[contains(.,'ADMIN')]").click()
#         self.driver.find_element_by_name("username").send_keys('admin')
#         self.driver.find_element_by_name("password").send_keys('1234')
#         self.driver.find_element_by_name("password").send_keys(Keys.ENTER)
#         self.driver.find_element_by_xpath("//a[contains(.,'View site')]").click()
#         # self.driver.findElement(By.xpath("//a[@href='/1/']")).click();
#         index_url = []
#         all_tag_a = self.driver.find_elements_by_tag_name("a")
#         for link in all_tag_a:
#             page_url = link.get_attribute('href')
#             index_url.append(page_url)
#         for i in index_url:
#             if i == "http://127.0.0.1:8000/1/":
#                 self.driver.get(i)
#         self.driver.find_element_by_name("borrow_amount").send_keys('1')
#         self.driver.find_element_by_xpath("//button[contains(.,'Confirm number')]").click()
#         time.sleep(1)
#         self.driver.find_element_by_name("borrow_date").send_keys('20-11-2021')
#         self.driver.find_element_by_xpath("//button[contains(.,'Confirm pick up date')]").click()
#         self.driver.find_element_by_name("return_date").send_keys('25-11-2021')
#         # self.driver.find_element_by_xpath("//button[contains(.,'Confirm')]").click()
#         borrow_amount_input = self.driver.find_element_by_name("borrow_amount")
#         assert borrow_amount_input != None
#
#     def test_borrow_date_input(self):
#         """Test can get into form which check by the user name."""
#         self.driver.find_element_by_xpath("//a[contains(.,'ADMIN')]").click()
#         self.driver.find_element_by_name("username").send_keys('admin')
#         self.driver.find_element_by_name("password").send_keys('1234')
#         self.driver.find_element_by_name("password").send_keys(Keys.ENTER)
#         self.driver.find_element_by_xpath("//a[contains(.,'View site')]").click()
#         # self.driver.findElement(By.xpath("//a[@href='/1/']")).click();
#         index_url = []
#         all_tag_a = self.driver.find_elements_by_tag_name("a")
#         for link in all_tag_a:
#             page_url = link.get_attribute('href')
#             index_url.append(page_url)
#         for i in index_url:
#             if i == "http://127.0.0.1:8000/1/":
#                 self.driver.get(i)
#         self.driver.find_element_by_name("borrow_amount").send_keys('1')
#         self.driver.find_element_by_xpath("//button[contains(.,'Confirm number')]").click()
#         time.sleep(1)
#         self.driver.find_element_by_name("borrow_date").send_keys('20-11-2021')
#         self.driver.find_element_by_xpath("//button[contains(.,'Confirm pick up date')]").click()
#         self.driver.find_element_by_name("return_date").send_keys('25-11-2021')
#         # self.driver.find_element_by_xpath("//button[contains(.,'Confirm')]").click()
#         borrow_date_input = self.driver.find_element_by_name("borrow_date")
#         assert borrow_date_input != None
#
#     def test_return_date_inputs(self):
#         """Test can get into form which check by the user name."""
#         self.driver.find_element_by_xpath("//a[contains(.,'ADMIN')]").click()
#         self.driver.find_element_by_name("username").send_keys('admin')
#         self.driver.find_element_by_name("password").send_keys('1234')
#         self.driver.find_element_by_name("password").send_keys(Keys.ENTER)
#         self.driver.find_element_by_xpath("//a[contains(.,'View site')]").click()
#         # self.driver.findElement(By.xpath("//a[@href='/1/']")).click();
#         index_url = []
#         all_tag_a = self.driver.find_elements_by_tag_name("a")
#         for link in all_tag_a:
#             page_url = link.get_attribute('href')
#             index_url.append(page_url)
#         for i in index_url:
#             if i == "http://127.0.0.1:8000/1/":
#                 self.driver.get(i)
#         self.driver.find_element_by_name("borrow_amount").send_keys('1')
#         self.driver.find_element_by_xpath("//button[contains(.,'Confirm number')]").click()
#         time.sleep(1)
#         self.driver.find_element_by_name("borrow_date").send_keys('20-11-2021')
#         self.driver.find_element_by_xpath("//button[contains(.,'Confirm pick up date')]").click()
#         self.driver.find_element_by_name("return_date").send_keys('25-11-2021')
#         # self.driver.find_element_by_xpath("//button[contains(.,'Confirm')]").click()
#         return_date_input = self.driver.find_element_by_name("return_date")
#         assert return_date_input != None
