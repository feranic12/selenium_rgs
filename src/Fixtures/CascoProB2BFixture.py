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
from Locators.CascoProB2BLocators import CascoProB2BLocators


class CascoProB2BFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-cascoProB2B.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CascoProB2BLocators.ButtonBuy1))
        element = driver.find_element(*CascoProB2BLocators.ButtonBuy1)
        element.click()

    def car_info(self):
        actions = self.actions
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(CascoProB2BLocators.Maker_Select))
        maker_select = Select(driver.find_element(*CascoProB2BLocators.Maker_Select))
        maker_select.select_by_index(1)
        model_select = Select(driver.find_element(*CascoProB2BLocators.Model_Select))
        model_select.select_by_index(1)
        element = driver.find_element(*CascoProB2BLocators.VIN)
        element.send_keys("11111111111111111")
        element = driver.find_element(*CascoProB2BLocators.Number)
        element.send_keys("А777АА77")
        element = driver.find_element(*CascoProB2BLocators.Pts_Seria)
        element.send_keys("1234")
        element = driver.find_element(*CascoProB2BLocators.Pts_Number)
        element.send_keys("123456")
        element = driver.find_element(*CascoProB2BLocators.Sts_Seria)
        element.send_keys("1234")
        element = driver.find_element(*CascoProB2BLocators.Sts_Number)
        element.send_keys("123456")
        element = driver.find_element(*CascoProB2BLocators.Continue_Button)
        element.click()

    def insurer_info(self):
        driver = self.driver
        element = driver.find_element(*CascoProB2BLocators.LastName)
        element.send_keys("Петров")
        element = driver.find_element(*CascoProB2BLocators.FirstName)
        element.send_keys("Пётр")
        element = driver.find_element(*CascoProB2BLocators.MiddleName)
        element.send_keys("Петрович")
        element = driver.find_element(*CascoProB2BLocators.Dob)
        element.send_keys("01011990")
        element = driver.find_element(*CascoProB2BLocators.Phone)
        element.send_keys("1231231212")
        element = driver.find_element(*CascoProB2BLocators.Male)
        element.click()
        element = driver.find_element(*CascoProB2BLocators.Email)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*CascoProB2BLocators.Email2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*CascoProB2BLocators.Passport_Seria)
        element.send_keys("1234")
        element = driver.find_element(*CascoProB2BLocators.Passport_Number)
        element.send_keys("123456")
        element = driver.find_element(*CascoProB2BLocators.Continue_Button)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable, CascoProB2BLocators.Accept_All_Input)
        element = driver.find_element(*CascoProB2BLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.car_info()
        #self.insurer_info()
        #self.agree()
