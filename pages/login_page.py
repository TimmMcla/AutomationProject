from helper.page import Page
from locators.locators import LoginPageLocators



class LoginPage(Page):

    def __init__(self):
        self.email_txtbox = LoginPageLocators.email_field
        self.password_txtbox = LoginPageLocators.password_field
        self.login_btn = LoginPageLocators.login_button


    def enter_email(self, email):
        self.find_by_selector(LoginPageLocators.email_field).sendKeys(email)

    def enter_password(self, password):
        self.find_by_selector(LoginPageLocators.password_field).sendKeys(password)

    def click_login(self):
        self.find_by_selector(LoginPageLocators.login_button).click()    
