from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains
import time
from utils import get_begin_day, enter_address_cdi
from Fixtures.BaseFixture import BaseFixture
from Locators.HouseflatLocators import HouseflatLocators


class HouseflatFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-houseflat.html"
        self.basic_setup(browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(HouseflatLocators.FlatButton))
        driver.find_element(*HouseflatLocators.FlatButton).click()
        element = driver.find_element(*HouseflatLocators.AddressCDI)
        enter_address_cdi(element, "г Москва, г Зеленоград, пл Юности, д 1")
        driver.find_element(*HouseflatLocators.Flat).send_keys("34")
        driver.find_element(*HouseflatLocators.Cadastre).send_keys("123123123")
        driver.find_element(*HouseflatLocators.Program5).click()
        driver.find_element(*HouseflatLocators.ContinueButton).click()

    def fill_frame(self):
        self.conditions()