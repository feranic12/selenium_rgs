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
from Locators.MyHealthLocators import MyHealthLocators


class MyHealthFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-myHealth.html"
        self.basic_setup(browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyHealthLocators.BuyButton))
        driver.find_element(*MyHealthLocators.BuyButton).click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyHealthLocators.InsurerLastname))
        driver.find_element(*MyHealthLocators.InsurerLastname).send_keys("Петров")
        driver.find_element(*MyHealthLocators.InsurerFirstname).send_keys("Пётр")
        driver.find_element(*MyHealthLocators.InsurerMiddlename).send_keys("Петрович")
        driver.find_element(*MyHealthLocators.InsurerDob).send_keys("01011990")
        driver.find_element(*MyHealthLocators.InsurerPhone).send_keys("1231231212")
        driver.find_element(*MyHealthLocators.MaleButton).click()
        driver.find_element(*MyHealthLocators.Email).send_keys("knikitin@avinfors.ru")
        driver.find_element(*MyHealthLocators.Email2).send_keys("knikitin@avinfors.ru")
        driver.find_element(*MyHealthLocators.PassportSeria).send_keys("1234")
        driver.find_element(*MyHealthLocators.PassportNumber).send_keys("123456")
        driver.find_element(*MyHealthLocators.ContinueButton).click()

    def insured_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyHealthLocators.ContinueButton))
        driver.find_element(*MyHealthLocators.ContinueButton).click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyHealthLocators.Accept))
        driver.find_element(*MyHealthLocators.Accept).click()

    def fill_frame(self):
        self.conditions()
        self.insurer_info()
        self.insured_info()
        self.agree()