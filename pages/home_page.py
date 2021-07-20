from helper.page import Page
from locators.locators import HomePageLocators


class HomePage(Page):
    
    def __init__(self):
        self.login_btn = HomePageLocators.login_button


    def click_login(self):
        self.find_by_selector(HomePageLocators.login_button).click()




