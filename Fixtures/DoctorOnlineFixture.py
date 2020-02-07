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
from Locators.DoctorOnlineLocators import DoctorOnlineLocators

class DoctorOnlineFixture(BaseFixture):
    def __init__(self, browser):
        target = r"https://testpartner.rgs.ru/b2c/product/build/test-telemedPlusB2B.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(DoctorOnlineLocators.ButtonBuy1))
        element = driver.find_element(*DoctorOnlineLocators.ButtonBuy1)
        element.click()

    def insurer(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(DoctorOnlineLocators.Surname))
        element = driver.find_element(*DoctorOnlineLocators.Surname)
        element.send_keys("Петров")
        element = driver.find_element(*DoctorOnlineLocators.First_Name)
        element.send_keys("Пётр")
        element = driver.find_element(*DoctorOnlineLocators.Middle_Name)
        element.send_keys("Петрович")
        element = driver.find_element(*DoctorOnlineLocators.DateOfBirth)
        element.send_keys("01011990")
        element = driver.find_element(*DoctorOnlineLocators.Phone)
        element.send_keys("1231231212")
        element = driver.find_element(*DoctorOnlineLocators.Male)
        element.click()
        element = driver.find_element(*DoctorOnlineLocators.EMail1)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*DoctorOnlineLocators.EMail2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*DoctorOnlineLocators.Seria)
        element.send_keys("1234")
        element = driver.find_element(*DoctorOnlineLocators.Number)
        element.send_keys("123456")
        element = driver.find_element(*DoctorOnlineLocators.Continue1)
        element.click()

    def insured(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(DoctorOnlineLocators.Is_Insurer))
        element = driver.find_element(*DoctorOnlineLocators.Continue2)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(DoctorOnlineLocators.Accept_All_Input))
        element = driver.find_element(*DoctorOnlineLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.insurer()
        self.insured()
        self.agree()