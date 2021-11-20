from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# URL to fetch and display

# create a browser instance. You can use Chrome or Safari instead of Firefox.
browser = webdriver.Chrome('/Users/whachanunya/Downloads/chromedriver')
url = "http://127.0.0.1:8000/admin/"
browser.get(url)
# browser.find_elements_by_tag_name("a")[1].click()

browser.find_element_by_id("id_username").send_keys("admin1")

browser.find_element_by_id("id_password").send_keys("123")

browser.find_element_by_id("id_password").send_keys(Keys.RETURN)

browser.find_elements_by_class_name("addlink")[4].click()

browser.find_element_by_id("id_item_name").send_keys("IPad")

browser.find_element_by_id("id_pickup_place").send_keys("Computer Department")

browser.find_element_by_id("id_owner").send_keys("Aj.Anan")

browser.find_element_by_id("id_note").send_keys("-")

browser.find_element_by_id("id_pub_date_0").send_keys("2021-11-09")
browser.find_element_by_id("id_pub_date_1").send_keys("08:49:19")

browser.find_element_by_id("id_item_image").send_keys(os.getcwd()+"/image.png")


browser.find_element_by_id("id_rate_fee").send_keys("1")

browser.find_element_by_id("id_max_item_each_user").send_keys("1")

browser.find_element_by_id("id_max_day_each_user").send_keys("7")

browser.find_element_by_id("id_max_day_each_user").send_keys(Keys.RETURN)
# # note: look at the browser window -- you can see the text
# # appear in the search field after you call send_keys()
# input_field.send_keys("Kasetsart University")
# input_field.send_keys(Keys.RETURN)

# elements: List[WebElement] = browser.find_elements_by_class_name("result__url")
# assert elements != None
# url = elements[0].get_attribute('href')
# elements[0].click()
# for link in elements:
#     if link.tag_name == 'a':
#         url = link.get_attribute('href')
#         print(url)