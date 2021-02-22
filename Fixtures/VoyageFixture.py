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
from Locators.VoyageLocators import VoyageLocators


class VoyageFixture(BaseFixture):
    def __init__(self, browser, days):
        self.days = days
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-voyage.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def insured_birthdates(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageLocators.Insured0_Dob_Input))
        element = driver.find_element(*VoyageLocators.Insured0_Dob_Input)
        element.send_keys("01011990")

    def trip_type(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(VoyageLocators.Trip_Type_Button))
        element = driver.find_element(*VoyageLocators.Trip_Type_Button)
        element.click()

    def country_select(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(VoyageLocators.Country_Input))
        element = driver.find_element(*VoyageLocators.Country_Input)
        element.send_keys("Дания"+Keys.ENTER)

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(VoyageLocators.Euro_Button))
        element = driver.find_element(*VoyageLocators.Euro_Button)
        element.click()
        element = driver.find_element(*VoyageLocators.F50000_Button)
        element.click()

    def trip_dates(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageLocators.Trip_Start_Input))
        element = driver.find_element(*VoyageLocators.Trip_Start_Input)
        element.send_keys(get_begin_day(self.days))
        element = driver.find_element(*VoyageLocators.Trip_End_Input)
        element.send_keys(get_begin_day(self.days+10))

    def protection(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageLocators.Protection_Needed_Button))
        element = driver.find_element(*VoyageLocators.Protection_Needed_Button)
        element.click()

    def buy_premium(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageLocators.Buy_Premium_Button))
        element = driver.find_element(*VoyageLocators.Buy_Premium_Button)
        element.click()

    def additional_options(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageLocators.No_Options_Button))
        element = driver.find_element(*VoyageLocators.No_Options_Button)
        element.click()

    def insured_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageLocators.Insured0_Lastname_Input))
        element = driver.find_element(*VoyageLocators.Insured0_Lastname_Input)
        element.send_keys("Петров")
        element = driver.find_element(*VoyageLocators.Insured0_Firstname_Input)
        element.send_keys("Пётр")
        element = driver.find_element(*VoyageLocators.Insured0_Middlename_Input)
        element.send_keys("Пётрович")
        element = driver.find_element(*VoyageLocators.Insured0_Lastname_Lat_Input)
        element.send_keys("Petrov")
        element = driver.find_element(*VoyageLocators.Insured0_Firstname_Lat_Input)
        element.send_keys("Petr")
        element = driver.find_element(*VoyageLocators.Insured0_Male_Button)
        element.click()
        element = driver.find_element(*VoyageLocators.Insured0_Document)
        element.send_keys("12 12345678")
        element = driver.find_element(*VoyageLocators.Insured0_Next_Button)
        element.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageLocators.Insurer_Firstname_Input))
        element = driver.find_element(*VoyageLocators.Insurer_Lastname_Input)
        element.send_keys("Петров")
        element = driver.find_element(*VoyageLocators.Insurer_Firstname_Input)
        element.send_keys("Пётр")
        element = driver.find_element(*VoyageLocators.Insurer_Middlename_Input)
        element.send_keys("Петрович")
        element = driver.find_element(*VoyageLocators.Insurer_Dob_Input)
        element.send_keys("01011990")
        element = driver.find_element(*VoyageLocators.Insurer_Phone_Input)
        element.send_keys("1231231212")
        element = driver.find_element(*VoyageLocators.Insurer_Document_Seria_Input)
        element.send_keys("1234")
        element = driver.find_element(*VoyageLocators.Insurer_Document_Number_Input)
        element.send_keys("123456")
        element = driver.find_element(*VoyageLocators.Insurer_Email_Input)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*VoyageLocators.Insurer_Email2_Input)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*VoyageLocators.Insurer_Next_Button)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageLocators.Accept_All_Input))
        element = driver.find_element(*VoyageLocators.Accept_All_Input)
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



