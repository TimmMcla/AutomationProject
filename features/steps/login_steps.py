from helper.driver_helper import DriverHelper
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from behave import given, when, then, step
from pages.home_page import HomePage
from pages.login_page import LoginPage

homePage = HomePage
loginPage = LoginPage

@given("user has navigated to Hudl.com")
def step_impl(context):
    context.driver.open("https://www.hudl.com")

@step("user clicks on the Login button")
def step_impl(context):
    homePage = HomePage(context)
    homePage.click_login
 

@when("user is taken to the Login page")
def step_impl(context):
   assert context.driver.current_url(), "https://www.hudl.com/login"

@step("user enters their valid credentials")
def step_impl(context):
    loginPage.enter_email(loginPage, "")
    loginPage.enter_password(loginPage, "")
    context.driver.find_by_selector("")



@when(u'user clicks the Login button')
def step_impl(context):
    loginPage.click_login()
    raise NotImplementedError(u'STEP: When user clicks the Login button')


@then(u'user is taken to their dashboard')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user is taken to their dashboard')


@when(u'user enters a valid email address')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user enters a valid email address')


@when(u'user enters an invalid password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When user enters an invalid password')


@then(u'user is presented with a "We didn\'t recognize that email and/or password. Need help?" error message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user is presented with a "We didn\'t recognize that email and/or password. Need help?" error message')


@then(u'user is unable to click the Login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then user is unable to click the Login button')



