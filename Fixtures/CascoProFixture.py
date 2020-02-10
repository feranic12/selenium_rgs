from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains
import time
from utils import get_begin_day
from Fixtures.BaseFixture import BaseFixture
from Locators.CascoProLocators import CascoProLocators

class CascoProFixture(BaseFixture):
    def __init__(self, browser):
        target = r"https://testpartner.rgs.ru/b2c/product/build/test-cascoProB2B.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CascoProLocators.ButtonBuy1))
        element = driver.find_element(*CascoProLocators.ButtonBuy1)
        element.click()

    def car_info(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(CascoProLocators.Mk))
        element = driver.find_element(*CascoProLocators.Mk)
        element.send_keys("Alfa Romeo"+Keys.ENTER*100)
        element = driver.find_element(*CascoProLocators.Model)
        element.send_keys("147"+Keys.ENTER*100)
        element = driver.find_element(*CascoProLocators.Year_Of_Issue)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.car_info()
