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
from Locators.MiteLocators import MiteLocators


class MiteFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-mite.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        #time.sleep(5)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MiteLocators.dob1))
        element = driver.find_element(*MiteLocators.dob1)
        element.send_keys("01011990" + Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MiteLocators.button2))
        element = driver.find_element(*MiteLocators.button2)
        element.click()

    def insured_info(self):
        driver = self.driver
        #driver.implicitly_wait(5)
        #time.sleep(2)
        element = driver.find_element(*MiteLocators.lastname)
        element.send_keys("Петров")
        element = driver.find_element(*MiteLocators.firstname)
        element.send_keys("Пётр")
        element = driver.find_element(*MiteLocators.middlename)
        element.send_keys("Петрович")
        element = driver.find_element(*MiteLocators.male)
        element.click()
        element = driver.find_element(*MiteLocators.is_insured)
        element.click()
        element = driver.find_element(*MiteLocators.Continue_Button1)
        element.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable, MiteLocators.phone)
        element = driver.find_element(*MiteLocators.phone)
        element.send_keys("1231231212")
        element = driver.find_element(*MiteLocators.email)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*MiteLocators.email2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*MiteLocators.seria)
        element.send_keys("1234")
        element = driver.find_element(*MiteLocators.number)
        element.send_keys("123456")
        element = driver.find_element(*MiteLocators.Continue_Button2)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable, MiteLocators.Accept_All_Input)
        element = driver.find_element(*MiteLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.insured_info()
        self.insurer_info()
        self.agree()
