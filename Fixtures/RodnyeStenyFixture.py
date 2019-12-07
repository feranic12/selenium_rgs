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
from Fixtures.Locators.RodnyeStenyLocators import RodnyeStenyLocators

class RodnyeStenyFixture(BaseFixture):
    def __init__(self, browser):
        target = r"https://testpartner.rgs.ru/b2c/product/build/test-flatbase.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RodnyeStenyLocators.Area_Input))
        element = driver.find_element(*RodnyeStenyLocators.Area_Input)
        element.send_keys("100")
        element = driver.find_element(*RodnyeStenyLocators.Region_Button)
        element.click()
        element = driver.find_element(*RodnyeStenyLocators.Owned_Button)
        element.click()
        element = driver.find_element(*RodnyeStenyLocators.Rent_Button)
        element.click()
        element = driver.find_element(*RodnyeStenyLocators.Fire_Button)
        element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RodnyeStenyLocators.Buy_Premium_Button))
        element = driver.find_element(*RodnyeStenyLocators.Buy_Premium_Button)
        element.click()

    def registration(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(RodnyeStenyLocators.Begin_Date_Input))
        element = driver.find_element(*RodnyeStenyLocators.Begin_Date_Input)
        element.send_keys(get_begin_day(10))
        element = driver.find_element(*RodnyeStenyLocators.Region_Input)
        element.send_keys("город.Москва"+Keys.ENTER)
        element = driver.find_element(*RodnyeStenyLocators.City_Input)
        element.send_keys("Москва")
        element = driver.find_element(*RodnyeStenyLocators.Street_Input)
        element.send_keys("Большая почтовая")
        element = driver.find_element(*RodnyeStenyLocators.House_Input)
        element.send_keys("1")
        element = driver.find_element(*RodnyeStenyLocators.Corp_Input)
        element.send_keys("2")
        element = driver.find_element(*RodnyeStenyLocators.Building_Input)
        element.send_keys("3")
        element = driver.find_element(*RodnyeStenyLocators.Flat_Input)
        element.send_keys("4")
        element = driver.find_element(*RodnyeStenyLocators.Calc_Next_Button)
        element.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(RodnyeStenyLocators.InsurersLastName_Input))
        element = driver.find_element(*RodnyeStenyLocators.InsurersLastName_Input)
        element.send_keys("Петров")
        element = driver.find_element(*RodnyeStenyLocators.InsurersFirstName_Input)
        element.send_keys("Пётр")
        element = driver.find_element(*RodnyeStenyLocators.InsurersMiddleName_Input)
        element.send_keys("Петрович")
        element = driver.find_element(*RodnyeStenyLocators.InsurersDob_Input)
        element.send_keys("01011990")
        element = driver.find_element(*RodnyeStenyLocators.InsurersPhone_Input)
        element.send_keys("1231231212")
        element = driver.find_element(*RodnyeStenyLocators.InsMale_Button)
        element.click()
        element = driver.find_element(*RodnyeStenyLocators.InsDocumentSeria_Input)
        element.send_keys("1234")
        element = driver.find_element(*RodnyeStenyLocators.InsDocumentNumber_Input)
        element.send_keys("123456")
        element = driver.find_element(*RodnyeStenyLocators.InsEmail_Input)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*RodnyeStenyLocators.InsEmail2_Input)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*RodnyeStenyLocators.Insurer_Next_Button)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RodnyeStenyLocators.Accept_All_Input))
        element = driver.find_element(*RodnyeStenyLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.registration()
        self.insurer_info()
        self.agree()