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
from Locators.EosagoLocators import EosagoLocators


class EosagoFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-eOsagoPolicy.html"
        self.basic_setup(browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def vehicle(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EosagoLocators.Capacity))
        driver.find_element(*EosagoLocators.Capacity).send_keys("120" + Keys.ENTER)
        driver.find_element(*EosagoLocators.Mark).click().send_keys("Acura" + Keys.ENTER)
        driver.find_element(*EosagoLocators.ProdYear).send_keys("2012")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EosagoLocators.Model))
        driver.find_element(*EosagoLocators.Model).send_keys("NSX" + Keys.ENTER)
        driver.find_element(*EosagoLocators.VIN).send_keys("12121212121212121")
        driver.find_element(*EosagoLocators.GosNumber).send_keys("А777АА77" + Keys.ENTER)
        driver.find_element(*EosagoLocators.StsSeria).send_keys("1234")
        driver.find_element(*EosagoLocators.StsNumber).send_keys("123456")
        driver.find_element(*EosagoLocators.StsDoi).send_keys("01012014")
        driver.find_element(*EosagoLocators.ContinueButton).click()

    def fill_frame(self):
        self.vehicle()
