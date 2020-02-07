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
from Locators.PoehaliLocators import PoehaliLocators


class PoehaliFixture(BaseFixture):
    def __init__(self, browser, days):
        self.days = days
        target = r"https://testpartner.rgs.ru/b2c/product/build/test-voyage.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def insured_birthdates(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PoehaliLocators.Insured0_Dob_Input))
        element = driver.find_element(*PoehaliLocators.Insured0_Dob_Input)
        element.send_keys("01012002")

    def trip_type(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PoehaliLocators.Trip_Type_Button))
        element = driver.find_element(*PoehaliLocators.Trip_Type_Button)
        element.click()

    def country_select(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(PoehaliLocators.Country_Input))
        element = driver.find_element(*PoehaliLocators.Country_Input)
        element.send_keys("Дания"+Keys.ENTER)

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(PoehaliLocators.Euro_Button))
        element = driver.find_element(*PoehaliLocators.Euro_Button)
        element.click()
        element = driver.find_element(*PoehaliLocators.F50000_Button)
        element.click()

    def trip_dates(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PoehaliLocators.Trip_Start_Input))
        element = driver.find_element(*PoehaliLocators.Trip_Start_Input)
        element.send_keys(get_begin_day(self.days))
        element = driver.find_element(*PoehaliLocators.Trip_End_Input)
        element.send_keys(get_begin_day(self.days+10))

    def protection(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PoehaliLocators.Protection_Needed_Button))
        element = driver.find_element(*PoehaliLocators.Protection_Needed_Button)
        element.click()

    def buy_premium(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PoehaliLocators.Buy_Premium_Button))
        element = driver.find_element(*PoehaliLocators.Buy_Premium_Button)
        element.click()

    def additional_options(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PoehaliLocators.No_Options_Button))
        element = driver.find_element(*PoehaliLocators.No_Options_Button)
        element.click()

    def insured_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PoehaliLocators.Insured0_Firstname_Input))
        element = driver.find_element(*PoehaliLocators.Insured0_Lastname_Input)
        element.send_keys("Петров")
        element = driver.find_element(*PoehaliLocators.Insured0_Firstname_Input)
        element.send_keys("Пётр")
        element = driver.find_element(*PoehaliLocators.Insured0_Middlename_Input)
        element.send_keys("Пётрович")
        element = driver.find_element(*PoehaliLocators.Insured0_Lastname_Lat_Input)
        element.send_keys("Petrov")
        element = driver.find_element(*PoehaliLocators.Insured0_Firstname_Lat_Input)
        element.send_keys("Petr")
        element = driver.find_element(*PoehaliLocators.Insured0_Male_Button)
        element.click()
        element = driver.find_element(*PoehaliLocators.Insured0_Document)
        element.send_keys("12 12345678")
        element = driver.find_element(*PoehaliLocators.Insured0_Next_Button)
        element.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PoehaliLocators.Insurer_Firstname_Input))
        element = driver.find_element(*PoehaliLocators.Insurer_Lastname_Input)
        element.send_keys("Петров")
        element = driver.find_element(*PoehaliLocators.Insurer_Firstname_Input)
        element.send_keys("Пётр")
        element = driver.find_element(*PoehaliLocators.Insurer_Middlename_Input)
        element.send_keys("Петрович")
        element = driver.find_element(*PoehaliLocators.Insurer_Dob_Input)
        element.send_keys("01011990")
        element = driver.find_element(*PoehaliLocators.Insurer_Phone_Input)
        element.send_keys("1231231212")
        element = driver.find_element(*PoehaliLocators.Insurer_Document_Seria_Input)
        element.send_keys("1234")
        element = driver.find_element(*PoehaliLocators.Insurer_Document_Number_Input)
        element.send_keys("123456")
        element = driver.find_element(*PoehaliLocators.Insurer_Email_Input)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*PoehaliLocators.Insurer_Email2_Input)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*PoehaliLocators.Insurer_Next_Button)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PoehaliLocators.Accept_All_Input))
        element = driver.find_element(*PoehaliLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.insured_birthdates()
        self.trip_type()
        self.country_select()
        self.conditions()
        self.trip_dates()
        self.protection()
        self.buy_premium()
        self.additional_options()
        self.insured_info()
        self.insurer_info()
        self.agree()



