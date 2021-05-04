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
from Locators.CarHelpLocators import CarHelpLocators


class CarHelpFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-carHelpB2B.html"
        BaseFixture.basic_setup(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CarHelpLocators.ButtonBuy1))
        element = driver.find_element(*CarHelpLocators.ButtonBuy1)
        element.click()

    def car_info(self):
        actions = self.actions
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(CarHelpLocators.Mk))
        element = driver.find_element(*CarHelpLocators.Mk)
        element.send_keys("Alfa Romeo"+Keys.ENTER*1000)
        element = driver.find_element(*CarHelpLocators.Model)
        element.send_keys("147"+Keys.ENTER*1000)
        element = driver.find_element(*CarHelpLocators.Year_Of_Issue)
        element.click()
        actions.move_by_offset(10,50).click().perform()
        element = driver.find_element(*CarHelpLocators.VIN)
        element.send_keys("11111111111111111")
        element = driver.find_element(*CarHelpLocators.Number)
        element.send_keys("А777АА77")
        element = driver.find_element(*CarHelpLocators.Pts_Seria)
        element.send_keys("1234")
        element = driver.find_element(*CarHelpLocators.Pts_Number)
        element.send_keys("123456")
        element = driver.find_element(*CarHelpLocators.Continue_Button)
        element.click()
        
    def insurer_info(self):
        driver = self.driver
        element = driver.find_element(*CarHelpLocators.LastName)
        element.send_keys("Петров")
        element = driver.find_element(*CarHelpLocators.FirstName)
        element.send_keys("Пётр")
        element = driver.find_element(*CarHelpLocators.MiddleName)
        element.send_keys("Петрович")
        element = driver.find_element(*CarHelpLocators.Dob)
        element.send_keys("01011990")
        element = driver.find_element(*CarHelpLocators.Phone)
        element.send_keys("1231231212")
        element = driver.find_element(*CarHelpLocators.Male)
        element.click()
        element = driver.find_element(*CarHelpLocators.Email)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*CarHelpLocators.Email2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*CarHelpLocators.Passport_Seria)
        element.send_keys("1234")
        element = driver.find_element(*CarHelpLocators.Passport_Number)
        element.send_keys("123456")
        element = driver.find_element(*CarHelpLocators.Continue_Button)
        element.click()
        
    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable, CarHelpLocators.Accept_All_Input)
        element = driver.find_element(*CarHelpLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.car_info()
        self.insurer_info()
        self.agree()
