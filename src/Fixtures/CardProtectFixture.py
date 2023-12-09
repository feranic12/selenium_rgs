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
from Locators.CardProtectLocators import CardProtectLocators


class CardProtectFixture(BaseFixture):
    def __init__(self, browser):
        self.target = "https://test2partner.rgs.ru/b2c/product/build/test-cardProtectPolicy.html?p=zenit"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable, CardProtectLocators.Buy_Button)
        driver.find_element(*CardProtectLocators.End_Date).send_keys("122024")
        driver.find_element(*CardProtectLocators.Buy_Button).click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable, CardProtectLocators.Continue_Button)
        driver.find_element(By.NAME, "content.policyHolder.lastName").send_keys("Петров")
        driver.find_element(By.NAME, "content.policyHolder.firstName").send_keys("Пётр")
        driver.find_element(By.NAME, "content.policyHolder.middleName").send_keys("Петрович")
        driver.find_element(By.NAME, "content.policyHolder.dob").send_keys("01011990")
        driver.find_element(By.NAME, "content.policyHolder.phone").send_keys("1231231212")
        driver.find_element(*CardProtectLocators.Male).click()
        driver.find_element(By.NAME, "content.policyHolder.email").send_keys("knikitin@avinfors.ru")
        driver.find_element(By.NAME, "content.policyHolder.email2").send_keys("knikitin@avinfors.ru")
        driver.find_element(By.NAME, "content.policyHolder.document.seria").send_keys("1234")
        driver.find_element(By.NAME, "content.policyHolder.document.number").send_keys("123456")
        driver.find_element(By.NAME, "content.policyHolder.document.doi").send_keys("01012019")
        driver.find_element(*CardProtectLocators.Continue_Button).click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable, CardProtectLocators.Accept)
        driver.find_element(*CardProtectLocators.Accept).click()

    def fill_frame(self):
        self.conditions()
        self.insurer_info()
        self.agree()