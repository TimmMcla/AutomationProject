from selenium import webdriver
from helper.driver_helper import DriverHelper


def get_browser(browser):
    if browser == "chrome":
        return DriverHelper(webdriver.Chrome("/home/timm/chromedriver_linux64/chromedriver"))