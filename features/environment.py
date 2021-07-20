from behave.fixture import use_fixture_by_tag
from selenium import webdriver
import os
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys
import time
from helper.fixtures import get_browser


def before_all(context):
    config = ConfigParser()
    my_config_file = (os.path.join(os.getcwd(), 'setup.cfg'))
    config.read(my_config_file)

    browser = get_browser(config.get('Environment', 'Browser'), config.get('Environment', 'Location'))
    context.driver = browser

def after_all(context):
    context.driver.close()