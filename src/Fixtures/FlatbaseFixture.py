from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains
import time
from utils import get_begin_day, enter_address_cdi
from Fixtures.BaseFixture import BaseFixture
from Locators.FlatbaseLocators import FlatbaseLocators


class FlatbaseFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-flatbase.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(FlatbaseLocators.Area_Input))
        element = driver.find_element(*FlatbaseLocators.Area_Input)
        element.send_keys("100")
        element = driver.find_element(*FlatbaseLocators.Region_Button)
        element.click()
        element = driver.find_element(*FlatbaseLocators.Owned_Button)
        element.click()
        element = driver.find_element(*FlatbaseLocators.Rent_Button)
        element.click()
        element = driver.find_element(*FlatbaseLocators.Fire_Button)
        element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(FlatbaseLocators.Buy_Premium_Button))
        element = driver.find_element(*FlatbaseLocators.Buy_Premium_Button)
        element.click()

    def registration(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(FlatbaseLocators.Begin_Date_Input))
        element = driver.find_element(*FlatbaseLocators.Begin_Date_Input)
        element.send_keys(get_begin_day(10))
        element = driver.find_element(*FlatbaseLocators.Address_CDI)
        enter_address_cdi(element, "г Москва, г Зеленоград, пл Юности, д 1" )
        element = driver.find_element(*FlatbaseLocators.Flat_Input)
        element.send_keys("4")
        element = driver.find_element(*FlatbaseLocators.Calc_Next_Button)
        element.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(FlatbaseLocators.InsurersLastName_Input))
        element = driver.find_element(*FlatbaseLocators.InsurersLastName_Input)
        element.send_keys("Петров")
        element = driver.find_element(*FlatbaseLocators.InsurersFirstName_Input)
        element.send_keys("Пётр")
        element = driver.find_element(*FlatbaseLocators.InsurersMiddleName_Input)
        element.send_keys("Петрович")
        element = driver.find_element(*FlatbaseLocators.InsurersDob_Input)
        element.send_keys("01011990")
        element = driver.find_element(*FlatbaseLocators.InsurersPhone_Input)
        element.send_keys("1231231212")
        element = driver.find_element(*FlatbaseLocators.InsMale_Button)
        element.click()
        element = driver.find_element(*FlatbaseLocators.InsDocumentSeria_Input)
        element.send_keys("1234")
        element = driver.find_element(*FlatbaseLocators.InsDocumentNumber_Input)
        element.send_keys("123456")
        element = driver.find_element(*FlatbaseLocators.InsEmail_Input)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*FlatbaseLocators.InsEmail2_Input)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*FlatbaseLocators.Insurer_Next_Button)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(FlatbaseLocators.Accept_All_Input))
        element = driver.find_element(*FlatbaseLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.registration()
        self.insurer_info()
        self.agree()