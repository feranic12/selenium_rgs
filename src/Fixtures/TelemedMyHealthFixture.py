import config
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from utils import get_begin_day
from Fixtures.BaseFixture import BaseFixture
from Locators.OncoProtectLocators import OncoProtectLocators


class TelemedMyHealthFixture(BaseFixture):
    def __init__(self, browser):
        self.target = "https://testpartner.rgs.ru/b2c/product/build/test-telemedMyHealth.html"
        self.basic_setup(browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))

    def conditions(self):
        driver = self.driver
        driver.find_element_by_xpath("//button[@type='button']").click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME("content.policyHolder.lastName"))))
        driver.find_element_by_name("content.policyHolder.lastName").click()
        driver.find_element_by_name("content.policyHolder.lastName").clear()
        driver.find_element_by_name("content.policyHolder.lastName").send_keys(u"Петров")
        driver.find_element_by_name("content.policyHolder.firstName").clear()
        driver.find_element_by_name("content.policyHolder.firstName").send_keys(u"Петр")
        driver.find_element_by_name("content.policyHolder.middleName").clear()
        driver.find_element_by_name("content.policyHolder.middleName").send_keys(u"Петрович")
        driver.find_element_by_xpath(
            "//div[@id='RI-product-steps']/div[2]/div/div[2]/div[5]/div/div/div/div/button").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='вс'])[1]/following::button[6]").click()
        driver.find_element_by_name("content.policyHolder.phone").click()
        driver.find_element_by_name("content.policyHolder.phone").clear()
        driver.find_element_by_name("content.policyHolder.phone").send_keys("+7(123)123-21-32")
        driver.find_element_by_xpath(
            "//div[@id='RI-product-steps']/div[2]/div/div[2]/div[7]/div/div/div/button").click()
        driver.find_element_by_name("content.policyHolder.email").click()
        driver.find_element_by_name("content.policyHolder.email").clear()
        driver.find_element_by_name("content.policyHolder.email").send_keys("knikitin@avinfors.ru")
        driver.find_element_by_name("content.policyHolder.email2").clear()
        driver.find_element_by_name("content.policyHolder.email2").send_keys("knikitin@avinfors.ru")
        driver.find_element_by_xpath("//div[@id='RI-product-steps']/div[2]/div/div[3]/div[2]/div").click()
        driver.find_element_by_name("content.policyHolder.document.seria").click()
        driver.find_element_by_name("content.policyHolder.document.seria").clear()
        driver.find_element_by_name("content.policyHolder.document.seria").send_keys("1234")
        driver.find_element_by_name("content.policyHolder.document.number").click()
        driver.find_element_by_name("content.policyHolder.document.number").clear()
        driver.find_element_by_name("content.policyHolder.document.number").send_keys("123123")
        driver.find_element_by_xpath("//div[@id='RI-product-steps']/div[2]/div/div[5]/button").click()

    def insured_info(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='RI-product-steps']/div[3]/div/div[2]/button").click()

    def agree(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='RI-product-steps']/div[4]/div/div/div/div/div/label").click()

    def fill_frame(self):
        driver = self.driver
        self.conditions()
        self.insurer_info()
        self.insured_info()
        self.agree()
