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
from Locators.MyStabilityLocators import MyStabilityLocators

class MyStabilityFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-myStability.html?p=open"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyStabilityLocators.BuyButton))
        driver.find_element(*MyStabilityLocators.BuyButton).click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "content.policyHolder.lastName")))
        driver.find_element(By.NAME, "content.policyHolder.lastName").send_keys("Петров")
        driver.find_element(By.NAME, "content.policyHolder.firstName").send_keys("Пётр")
        driver.find_element(By.NAME, "content.policyHolder.middleName").send_keys("Петрович")
        driver.find_element(By.NAME, "content.policyHolder.dob").send_keys("01011990")
        driver.find_element(By.NAME, "content.policyHolder.phone").send_keys("1231231212")
        driver.find_element(*MyStabilityLocators.MaleButton).click()
        driver.find_element(By.NAME, "content.policyHolder.email").send_keys("knikitin@avinfors.ru")
        driver.find_element(By.NAME, "content.policyHolder.email2").send_keys("knikitin@avinfors.ru")
        driver.find_element(By.NAME, "content.policyHolder.document.seria").send_keys("1234")
        driver.find_element(By.NAME, "content.policyHolder.document.number").send_keys("123456")
        driver.find_element(*MyStabilityLocators.ContinueButton).click()

    def insured_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyStabilityLocators.Accept1))
        driver.find_element(*MyStabilityLocators.Accept1).click()
        driver.find_element(*MyStabilityLocators.Accept2).click()

    def fill_frame(self):
        self.conditions()
        self.insurer_info()
        self.insured_info()