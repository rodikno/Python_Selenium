# -*- coding: utf-8 -*-
from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

# driver = webdriver.Chrome()
# driver.get('https://google.com.ua')
# search_bar = driver.find_element_by_css_selector('input.gsfi')
# search_bar.send_keys('Hello World')
# search_bar.send_keys(Keys.RETURN)
# time.sleep(5)
# driver.quit()

@given('user is on the login page')
def step(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get("https://www.google.com.ua/")

@when('I log in with correct credentials')
def step(context):
