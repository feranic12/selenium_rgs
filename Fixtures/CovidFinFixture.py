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
from Locators.CovidFinLocators import CovidFinLocators


class CovidFinFixture(BaseFixture):
    def __init__(self, browser):
        target = r"https://testpartner.rgs.ru/b2c/product/build/test-covidFin.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def first_block(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CovidFinLocators.male))
        element = driver.find_element(*CovidFinLocators.dob)
        element.send_keys("01011980")
        element = driver.find_element(*CovidFinLocators.male)
        element.click()
        element = driver.find_element(*CovidFinLocators.is_insured)
        element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CovidFinLocators.insured_dob))
        element = driver.find_element(*CovidFinLocators.insured_dob)
        element.send_keys("01011970")
        element = driver.find_element(*CovidFinLocators.insured_male)
        element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CovidFinLocators.button1))
        element = driver.find_element(*CovidFinLocators.button1)
        element.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CovidFinLocators.insurer_lastname))
        element = driver.find_element(*CovidFinLocators.insurer_lastname)
        element.send_keys("Петров")
        element = driver.find_element(*CovidFinLocators.insurer_firstname)
        element.send_keys("Петр")
        element = driver.find_element(*CovidFinLocators.insurer_middlename)
        element.send_keys("Петрович")
        element = driver.find_element(*CovidFinLocators.insurer_phone)
        element.send_keys("1231231212")
        element = driver.find_element(*CovidFinLocators.insurer_email)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*CovidFinLocators.insurer_email2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*CovidFinLocators.insurer_seria)
        element.send_keys("1234")
        element = driver.find_element(*CovidFinLocators.insurer_number)
        element.send_keys("123123")
        element = driver.find_element(*CovidFinLocators.continue_button)
        element.click()

    def insured_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CovidFinLocators.insured_lastname))
        element = driver.find_element(*CovidFinLocators.insured_lastname)
        element.send_keys("Петров")
        element = driver.find_element(*CovidFinLocators.insured_firstname)
        element.send_keys("Петр")
        element = driver.find_element(*CovidFinLocators.insured_middlename)
        element.send_keys("Петрович")
        element = driver.find_element(*CovidFinLocators.insured_phone)
        element.send_keys("1231231212")
        element = driver.find_element(*CovidFinLocators.insured_email)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*CovidFinLocators.insured_document_type)
        element.send_keys("Паспорт"+Keys.ENTER)
        element = driver.find_element(*CovidFinLocators.insured_seria)
        element.send_keys("1234")
        element = driver.find_element(*CovidFinLocators.insured_number)
        element.send_keys("123123")
        element = driver.find_element(*CovidFinLocators.continue_button)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable, CovidFinLocators.Accept_All_Input)
        element = driver.find_element(*CovidFinLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.first_block()
        self.insurer_info()
        self.insured_info()
        self.agree()


