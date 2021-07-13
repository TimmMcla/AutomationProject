from helper.driver_helper import DriverHelper
from locators.locators import LoginPageLocators



class LoginPage():

    def __init__(self):
        self.email_txtbox = LoginPageLocators.email_field
        self.password_txtbox = LoginPageLocators.password_field
        self.login_btn = LoginPageLocators.login_button


    def enter_email(self, email):
        DriverHelper.find_by_selector(LoginPageLocators.email_field).sendKeys(email)

    def enter_password(self, password):
        DriverHelper.find_by_selector(LoginPageLocators.password_field).sendKeys(password)

    def click_login(self):
        DriverHelper.find_by_selector(LoginPageLocators.login_button).click()    
