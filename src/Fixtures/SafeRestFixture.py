from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains
import time
from utils import get_begin_day
from Fixtures.BaseFixture import BaseFixture
from Locators.SafeRestLocators import SafeRestLocators


class SafeRestFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://test2partner.rgs.ru/b2c/product/build/test-safeRest.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SafeRestLocators.InsuredDob))
        driver.find_element(*SafeRestLocators.InsuredDob).send_keys("01011990")
        driver.find_element(*SafeRestLocators.Term).send_keys("10")
        driver.find_element(*SafeRestLocators.MiteRisk).click()
        driver.find_element(*SafeRestLocators.MedicalRisk).click()
        driver.find_element(*SafeRestLocators.AccidentRisk).click()
        driver.find_element(*SafeRestLocators.SportOption).click()
        driver.find_element(*SafeRestLocators.AlcOption).click()
        driver.find_element(*SafeRestLocators.IllOption).click()
        driver.find_element(*SafeRestLocators.ContinueButton).click()

    def insured0_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SafeRestLocators.Insured0LastName))
        driver.find_element(*SafeRestLocators.Insured0LastName).send_keys("Петров")
        driver.find_element(*SafeRestLocators.Insured0FirstName).send_keys("Пётр")
        driver.find_element(*SafeRestLocators.Insured0MiddleName).send_keys("Петрович")
        driver.find_element(*SafeRestLocators.ContinueButton).click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SafeRestLocators.InsurersPhone))
        driver.find_element(*SafeRestLocators.InsurersPhone).send_keys("1231231212")
        driver.find_element(*SafeRestLocators.InsurersMale).click()
        driver.find_element(*SafeRestLocators.InsurersEmail).send_keys(("knikitin@avinfors.ru"))
        driver.find_element(*SafeRestLocators.InsurersEmail2).send_keys(("knikitin@avinfors.ru"))
        driver.find_element(*SafeRestLocators.ContinueButton).click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SafeRestLocators.Agree))
        driver.find_element(*SafeRestLocators.Agree).click()

    def fill_frame(self):
        self.conditions()
        self.insured0_info()
        self.insurer_info()
        self.agree()
