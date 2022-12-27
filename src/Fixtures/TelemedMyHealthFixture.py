import config
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from utils import get_begin_day
from Fixtures.BaseFixture import BaseFixture
from Locators.TelemedMyHealthLocators import TelemedMyHealthLocators


class TelemedMyHealthFixture(BaseFixture):
    def __init__(self, browser):
        self.target = "https://test2partner.rgs.ru/b2c/product/build/test-telemedMyHealth.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TelemedMyHealthLocators.BuyButton))
        driver.find_element(*TelemedMyHealthLocators.BuyButton).click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TelemedMyHealthLocators.InsurerLastName))
        driver.find_element(*TelemedMyHealthLocators.InsurerLastName).send_keys(u"Петров")
        driver.find_element(*TelemedMyHealthLocators.InsurerFirstName).send_keys(u"Петр")
        driver.find_element(*TelemedMyHealthLocators.InsurerMiddleName).send_keys(u"Петрович")
        driver.find_element(*TelemedMyHealthLocators.InsurerDob).send_keys("01011990")
        driver.find_element(*TelemedMyHealthLocators.InsurerMale).click()
        driver.find_element(*TelemedMyHealthLocators.InsurerPhone).send_keys("+7(123)123-21-32")
        driver.find_element(*TelemedMyHealthLocators.InsurerEMail).send_keys("knikitin@avinfors.ru")
        driver.find_element(*TelemedMyHealthLocators.InsurerEMail2).send_keys("knikitin@avinfors.ru")
        driver.find_element(*TelemedMyHealthLocators.InsurerPassportSeria).send_keys("1234")
        driver.find_element(*TelemedMyHealthLocators.InsurerPassportNumber).send_keys("123123")
        driver.find_element(*TelemedMyHealthLocators.ContinueButton).click()

    def insured_info(self):
        driver = self.driver
        driver.find_element(*TelemedMyHealthLocators.ContinueButton2).click()

    def agree(self):
        driver = self.driver
        driver.find_element(*TelemedMyHealthLocators.Agree).click()

    def fill_frame(self):
        driver = self.driver
        self.conditions()
        self.insurer_info()
        self.insured_info()
        self.agree()
