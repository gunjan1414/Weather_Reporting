import logging
from configparser import ConfigParser
from pathlib import Path

from utilities.Driver import Driver

driver = None


class Login:
    @staticmethod
    def login(context):
        path = Path('..').cwd().as_posix()
        login_path = path + '/properties/' + 'config' +'.properties'
        login_parser = ConfigParser()
        login_parser.read(login_path)
        url = login_parser.get("config", "url")
        Login.login_code(context, url)

    @staticmethod
    def login_code(context, url):
        global driver
        try:
            driver = Driver.return_driver()
            driver.maximize_window()  # Maximize the window
            logging.info("Maximize the window")
            driver.get(url)  # Getting the base URl homepage
            logging.info("Opening the web url " + url)
        except Exception as inst:
            logging.info(str(inst))