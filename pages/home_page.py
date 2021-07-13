from helper.driver_helper import DriverHelper
from locators.locators import HomePageLocators

class HomePage(object):
    
    def __init__(self, driver):
        self.login_btn = HomePageLocators.login_button
        self.driver = driver


    def click_login(self):
        self.driver(self.login_btn).click




