from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains
import time
from Fixtures.BaseFixture import BaseFixture
from Locators.NoPanicLocators import NoPanicLocators


class NoPanicFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-nopanic.html"
        BaseFixture.basic_setup(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def first_block(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NoPanicLocators.male))
        element = driver.find_element(*NoPanicLocators.dob)
        element.send_keys("01011980")
        element = driver.find_element(*NoPanicLocators.male)
        element.click()
        element = driver.find_element(*NoPanicLocators.button1)
        element.click()
        
    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NoPanicLocators.insurer_lastname))
        element = driver.find_element(*NoPanicLocators.insurer_lastname)
        element.send_keys("Петров")
        element = driver.find_element(*NoPanicLocators.insurer_firstname)
        element.send_keys("Петр")
        element = driver.find_element(*NoPanicLocators.insurer_middlename)
        element.send_keys("Петрович")
        element = driver.find_element(*NoPanicLocators.insurer_phone)
        element.send_keys("1231231212")
        element = driver.find_element(*NoPanicLocators.insurer_email)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*NoPanicLocators.insurer_email2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*NoPanicLocators.insurer_seria)
        element.send_keys("1234")
        element = driver.find_element(*NoPanicLocators.insurer_number)
        element.send_keys("123123")
        element = driver.find_element(*NoPanicLocators.continue_button)
        element.click()
        
    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable, NoPanicLocators.Accept_All_Input)
        element = driver.find_element(*NoPanicLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.first_block()
        self.insurer_info()
        self.agree()


