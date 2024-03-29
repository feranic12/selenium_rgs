from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
from utils import get_begin_day, enter_address_new1
from Fixtures.BaseFixture import BaseFixture
from Locators.GoodChoiceB2BLocators import GoodChoiceB2BLocators


class GoodChoiceB2BFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://test2partner.rgs.ru/b2c/product/build/test-goodChoiceB2B.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def policy_type(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(GoodChoiceB2BLocators.Button_Prolongation_False))
        element = driver.find_element(*GoodChoiceB2BLocators.Button_Prolongation_False)
        element.click()

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(GoodChoiceB2BLocators.Button1))
        element = driver.find_element(*GoodChoiceB2BLocators.Button1)
        element.click()

    def insurance_object(self):
        driver = self.driver
        element = driver.find_element(*GoodChoiceB2BLocators.AddressNew1)
        enter_address_new1(element, "г Москва", ActionChains(driver), 300, 500)
        driver.find_element(*GoodChoiceB2BLocators.AddressNew2).send_keys("Площадь Юности, д 34" + Keys.ENTER)
        #element = driver.find_element(*GoodChoiceB2BLocators.Flat)
        #element.send_keys("15")
        element = driver.find_element(*GoodChoiceB2BLocators.Continue_Button2)
        element.click()

    def insurer(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(GoodChoiceB2BLocators.Surname))
        element = driver.find_element(*GoodChoiceB2BLocators.Surname)
        element.send_keys("Петров")
        element = driver.find_element(*GoodChoiceB2BLocators.First_Name)
        element.send_keys("Пётр")
        element = driver.find_element(*GoodChoiceB2BLocators.Middle_Name)
        element.send_keys("Петрович")
        element = driver.find_element(*GoodChoiceB2BLocators.Dob)
        element.send_keys("01011990")
        element = driver.find_element(*GoodChoiceB2BLocators.Phone)
        element.send_keys("1231231212")
        element = driver.find_element(*GoodChoiceB2BLocators.EMail1)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*GoodChoiceB2BLocators.EMail2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*GoodChoiceB2BLocators.Passport_Seria)
        element.send_keys("1234")
        element = driver.find_element(*GoodChoiceB2BLocators.Passport_Number)
        element.send_keys("123456")
        #element = driver.find_element(*GoodChoiceB2BLocators.Passport_Date)
        #element.send_keys("01012010")
        #element = driver.find_element(*GoodChoiceB2BLocators.Passport_Issued)
        #element.send_keys("ОВД")
        #element = driver.find_element(*GoodChoiceB2BLocators.Passport_Department)
        #element.send_keys("123123")
        #element = driver.find_element(*GoodChoiceB2BLocators.Citizenship)
        #element.send_keys("РФ")
        #element = driver.find_element(*GoodChoiceB2BLocators.SNILS)
        #element.send_keys("1231231231212")
        #element = driver.find_element(*GoodChoiceB2BLocators.INN)
        #element.send_keys("111111111130")
        #element = driver.find_element(*GoodChoiceB2BLocators.Birth_Place)
        #element.send_keys("Россия")
        element = driver.find_element(*GoodChoiceB2BLocators.Continue_Button3)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(GoodChoiceB2BLocators.Accept_All_Input))
        element = driver.find_element(*GoodChoiceB2BLocators.Accept_All_Input)
        element.click()

    def fill_frame(self):
        self.policy_type()
        self.conditions()
        self.insurance_object()
        self.insurer()
        self.agree()