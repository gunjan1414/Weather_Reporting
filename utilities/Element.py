import logging
from datetime import time
from pathlib import Path
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.Driver import Driver

driver = None
result_value = None


class Element:
    @staticmethod
    def click(context, obj):
        global driver
        driver = Driver.return_driver()
        path = Path('..').cwd().as_posix()
        element = path.cf_parser.get("xpath", obj)
        click_element = driver.find_element_by_xpath(element)
        try:
            click_element.click()
        except Exception as inst:
            logging.info(str(inst))

    @staticmethod
    def input(context, text, obj):
        global driver
        driver = Driver.return_driver()
        path = Path('..').cwd().as_posix()
        element = path.cf_parser.get("xpath", obj)
        time.sleep(2)
        try:
            # Element.pop_up_handle(context, obj)
            WebDriverWait(driver, 90).until(ec.element_to_be_clickable((By.XPATH, element)))
            driver.find_element_by_xpath(element).send_keys(text)
        except Exception as inst:
            logging.info(str(inst))

    @staticmethod
    def get_text_for_all(context, obj):
        global driver
        driver = Driver.return_driver()
        path = Path('..').cwd().as_posix()
        try:
            element = path.cf_parser.get("xpath", obj)
            # result = driver.find_element_by_xpath(element).text
            result = driver.find_element_by_xpath(element).get_attribute("value")
            return result
        except Exception as inst:
            logging.info(str(inst))