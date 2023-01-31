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
from Locators.CascoProLocators import CascoProLocators


class CascoProB2BFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-cascoProB2B.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CascoProLocators.ButtonBuy1))
        element = driver.find_element(*CascoProLocators.ButtonBuy1)
        element.click()

    def car_info(self):
        actions = self.actions
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(CascoProLocators.Maker_Select))
        maker_select = Select(driver.find_element(*CascoProLocators.Maker_Select))
        maker_select.select_by_index(1)
        model_select = Select(driver.find_element(*CascoProLocators.Model_Select))
        model_select.select_by_index(1)
        element = driver.find_element(*CascoProLocators.VIN)
        element.send_keys("11111111111111111")
        element = driver.find_element(*CascoProLocators.Number)
        element.send_keys("А777АА77")
        element = driver.find_element(*CascoProLocators.Pts_Seria)
        element.send_keys("1234")
        element = driver.find_element(*CascoProLocators.Pts_Number)
        element.send_keys("123456")
        element = driver.find_element(*CascoProLocators.Sts_Seria)
        element.send_keys("1234")
        element = driver.find_element(*CascoProLocators.Sts_Number)
        element.send_keys("123456")
        element = driver.find_element(*CascoProLocators.Continue_Button)
        element.click()

    def insurer_info(self):
        driver = self.driver
        element = driver.find_element(*CascoProLocators.LastName)
        element.send_keys("Петров")
        element = driver.find_element(*CascoProLocators.FirstName)
        element.send_keys("Пётр")
        element = driver.find_element(*CascoProLocators.MiddleName)
        element.send_keys("Петрович")
        element = driver.find_element(*CascoProLocators.Dob)
        element.send_keys("01011990")
        element = driver.find_element(*CascoProLocators.Phone)
        element.send_keys("1231231212")
        element = driver.find_element(*CascoProLocators.Male)
        element.click()
        element = driver.find_element(*CascoProLocators.Email)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*CascoProLocators.Email2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*CascoProLocators.Passport_Seria)
        element.send_keys("1234")
        element = driver.find_element(*CascoProLocators.Passport_Number)
        element.send_keys("123456")
        element = driver.find_element(*CascoProLocators.Continue_Button)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable, CascoProLocators.Accept_All_Input)
        element = driver.find_element(*CascoProLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.car_info()
        #self.insurer_info()
        #self.agree()
