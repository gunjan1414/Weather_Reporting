from requests import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
driver = None


class Driver:

    @staticmethod
    def open_browser():
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver

    @staticmethod
    def return_driver():
        return driver
