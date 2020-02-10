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
from Locators.GoodChoiceLocators import GoodChoiceLocators


class GoodChoiceFixture(BaseFixture):
    def __init__(self, browser):
        target = r"https://testpartner.rgs.ru/b2c/product/build/test-goodChoiceB2B.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        element = driver.find_element(*GoodChoiceLocators.Button1)
        element.click()

    def insurance_object(self):
        driver = self.driver
        #WebDriverWait(driver,10).until(EC.element_to_be_clickable(GoodChoiceLocators.Button_Flat))
        #element = driver.find_element(*GoodChoiceLocators.Button_Flat)
        #element.click()
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(GoodChoiceLocators.Region_Input))
        element = driver.find_element(*GoodChoiceLocators.Region_Input)
        element.send_keys("город.Москва" + Keys.ENTER)
        element = driver.find_element(*GoodChoiceLocators.City)
        element.send_keys("Москва")
        element = driver.find_element(*GoodChoiceLocators.Street)
        element.send_keys("ул.Ленина")
        element = driver.find_element(*GoodChoiceLocators.House)
        element.send_keys("12")
        element = driver.find_element(*GoodChoiceLocators.Corp)
        element.send_keys("13")
        element = driver.find_element(*GoodChoiceLocators.Building)
        element.send_keys("14")
        #element = driver.find_element(*GoodChoiceLocators.Flat)
        #element.send_keys("15")
        element = driver.find_element(*GoodChoiceLocators.Continue_Button1)
        element.click()

    def insurer(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(GoodChoiceLocators.Surname))
        element = driver.find_element(*GoodChoiceLocators.Surname)
        element.send_keys("Петров")
        element = driver.find_element(*GoodChoiceLocators.First_Name)
        element.send_keys("Пётр")
        element = driver.find_element(*GoodChoiceLocators.Middle_Name)
        element.send_keys("Петрович")
        element = driver.find_element(*GoodChoiceLocators.Dob)
        element.send_keys("01011990")
        element = driver.find_element(*GoodChoiceLocators.Phone)
        element.send_keys("1231231212")
        element = driver.find_element(*GoodChoiceLocators.Male)
        element.click()
        element = driver.find_element(*GoodChoiceLocators.EMail1)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*GoodChoiceLocators.EMail2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*GoodChoiceLocators.Passport_Seria)
        element.send_keys("1234")
        element = driver.find_element(*GoodChoiceLocators.Passport_Number)
        element.send_keys("123456")
        #element = driver.find_element(*GoodChoiceLocators.Passport_Date)
        #element.send_keys("01012010")
        #element = driver.find_element(*GoodChoiceLocators.Passport_Issued)
        #element.send_keys("ОВД")
        #element = driver.find_element(*GoodChoiceLocators.Passport_Department)
        #element.send_keys("123123")
        #element = driver.find_element(*GoodChoiceLocators.Citizenship)
        #element.send_keys("РФ")
        #element = driver.find_element(*GoodChoiceLocators.SNILS)
        #element.send_keys("1231231231212")
        #element = driver.find_element(*GoodChoiceLocators.INN)
        #element.send_keys("111111111130")
        #element = driver.find_element(*GoodChoiceLocators.Birth_Place)
        #element.send_keys("Россия")
        element = driver.find_element(*GoodChoiceLocators.Continue_Button2)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(GoodChoiceLocators.Accept_All_Input))
        element = driver.find_element(*GoodChoiceLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.insurance_object()
        self.insurer()
        self.agree()