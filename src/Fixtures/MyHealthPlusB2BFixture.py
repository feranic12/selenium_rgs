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
from Locators.MyHealthPlusB2BLocators import MyHealthPlusB2BLocators


class MyHealthPlusB2BFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-MyHealthPlusB2B.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyHealthPlusB2BLocators.BuyButton))
        driver.find_element(*MyHealthPlusB2BLocators.BuyButton).click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyHealthPlusB2BLocators.InsurerLastname))
        driver.find_element(*MyHealthPlusB2BLocators.InsurerLastname).send_keys("Петров")
        driver.find_element(*MyHealthPlusB2BLocators.InsurerFirstname).send_keys("Пётр")
        driver.find_element(*MyHealthPlusB2BLocators.InsurerMiddlename).send_keys("Петрович")
        driver.find_element(*MyHealthPlusB2BLocators.InsurerDob).send_keys("01011990")
        driver.find_element(*MyHealthPlusB2BLocators.InsurerPhone).send_keys("1231231212")
        driver.find_element(*MyHealthPlusB2BLocators.MaleButton).click()
        driver.find_element(*MyHealthPlusB2BLocators.Email).send_keys("knikitin@avinfors.ru")
        driver.find_element(*MyHealthPlusB2BLocators.Email2).send_keys("knikitin@avinfors.ru")
        driver.find_element(*MyHealthPlusB2BLocators.PassportSeria).send_keys("1234")
        driver.find_element(*MyHealthPlusB2BLocators.PassportNumber).send_keys("123456")
        driver.find_element(*MyHealthPlusB2BLocators.ContinueButton).click()

    def insured_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyHealthPlusB2BLocators.ContinueButton))
        driver.find_element(*MyHealthPlusB2BLocators.ContinueButton).click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyHealthPlusB2BLocators.Accept))
        driver.find_element(*MyHealthPlusB2BLocators.Accept).click()

    def fill_frame(self):
        self.conditions()
        self.insurer_info()
        self.insured_info()
        self.agree()