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
from Locators.GetVaccineLocators import GetVaccineLocators


class GetVaccineFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-getVaccine.html"
        BaseFixture.basic_setup(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(GetVaccineLocators.ButtonBuy))
        element = driver.find_element(*GetVaccineLocators.ButtonBuy)
        element.click()

    def insurer_info(self):
        driver = self.driver
        element = driver.find_element(*GetVaccineLocators.IsInsured)
        element.click()
        element = driver.find_element(*GetVaccineLocators.InsurersLastname)
        element.send_keys("Петров")
        element = driver.find_element(*GetVaccineLocators.InsurersFirstname)
        element.send_keys("Петр")
        element = driver.find_element(*GetVaccineLocators.InsurersMiddlename)
        element.send_keys("Петрович")
        element = driver.find_element(*GetVaccineLocators.InsurersDob)
        element.send_keys("01011990")
        element = driver.find_element(*GetVaccineLocators.InsurerMale)
        element.click()
        element = driver.find_element(*GetVaccineLocators.InsurersPhone)
        element.send_keys("1231231212")
        element = driver.find_element(*GetVaccineLocators.InsurersEmail)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*GetVaccineLocators.InsurersEmail2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*GetVaccineLocators.InsurersPassportSeria)
        element.send_keys("1234")
        element = driver.find_element(*GetVaccineLocators.InsurersPassportNumber)
        element.send_keys("123456")
        element = driver.find_element(*GetVaccineLocators.ContinueButton)
        element.click()

    def agree(self):
        driver = self.driver
        element = driver.find_element(*GetVaccineLocators.AcceptAllInput)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.insurer_info()
        self.agree()