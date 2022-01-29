from jmespath import search
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import bs4
from selenium import webdriver


def lol(q):
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.linkedin.com/search/results/all/?keywords=' + q)
    return driver.find_element_by_name('https://www.linkedin.com/')

print(lol("sehas"))

