from selenium import webdriver
from helper.page import Page


def get_browser(browser, location):
    if browser == "chrome":
        return Page(webdriver.Chrome(location))