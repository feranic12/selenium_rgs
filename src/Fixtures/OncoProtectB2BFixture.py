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
from Locators.OncoProtectB2BLocators import OncoProtectB2BLocators


class OncoProtectB2BFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-oncoProtectB2B.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def policy_type(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(OncoProtectB2BLocators.Button_Prolongation_False))
        element = driver.find_element(*OncoProtectB2BLocators.Button_Prolongation_False)
        element.click()

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(OncoProtectB2BLocators.ButtonBuy1))
        element = driver.find_element(*OncoProtectB2BLocators.ButtonBuy1)
        element.click()

    def insurer(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(OncoProtectB2BLocators.Surname))
        element = driver.find_element(*OncoProtectB2BLocators.Surname)
        element.send_keys("Петров")
        element = driver.find_element(*OncoProtectB2BLocators.First_Name)
        element.send_keys("Пётр")
        element = driver.find_element(*OncoProtectB2BLocators.Middle_Name)
        element.send_keys("Петрович")
        element = driver.find_element(*OncoProtectB2BLocators.DateOfBirth)
        element.send_keys("01011990")
        element = driver.find_element(*OncoProtectB2BLocators.Phone)
        element.send_keys("1231231212")
        element = driver.find_element(*OncoProtectB2BLocators.Male)
        element.click()
        element = driver.find_element(*OncoProtectB2BLocators.EMail1)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*OncoProtectB2BLocators.EMail2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*OncoProtectB2BLocators.Seria)
        element.send_keys("1234")
        element = driver.find_element(*OncoProtectB2BLocators.Number)
        element.send_keys("123456")
        element = driver.find_element(*OncoProtectB2BLocators.Continue_Button2)
        element.click()

    def insured(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(OncoProtectB2BLocators.Is_Insurer))
        element = driver.find_element(*OncoProtectB2BLocators.Continue_Button3)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(OncoProtectB2BLocators.Accept_All_Input))
        element = driver.find_element(*OncoProtectB2BLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.policy_type()
        self.conditions()
        self.insurer()
        self.insured()
        self.agree()
