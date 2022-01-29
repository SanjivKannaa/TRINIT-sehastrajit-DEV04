from time import sleep
import parameters
from jmespath import search
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import bs4
from selenium import webdriver
import csv

# defining new variable passing two parameters
writer = csv.writer(open(parameters.file_name, 'wb'))

# writerow() method to the write to the file object
writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/Users/username/bin/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element_by_class_name('login-email')

# send_keys() to simulate key strokes
username.send_keys(parameters.linkedin_username)

# sleep for 0.5 seconds
sleep(0.5)

# locate password form by_class_name
password = driver.find_element_by_class_name('login-password')

# send_keys() to simulate key strokes
password.send_keys(parameters.linkedin_password)
sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()