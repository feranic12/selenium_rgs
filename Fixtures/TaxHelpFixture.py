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
from Locators.TaxHelpLocators import TaxHelpLocators



class TaxHelpFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-taxHelp.html"
        self.basic_setup(browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TaxHelpLocators.BuyButton))
        driver.find_element(*TaxHelpLocators.BuyButton).click()

    def insurer_info(self):
        driver = self.driver
        driver.find_element_by_name("content.policyHolder.lastName").send_keys(u"Петров")
        driver.find_element_by_name("content.policyHolder.firstName").send_keys(u"Петр")
        driver.find_element_by_name("content.policyHolder.middleName").send_keys(u"Петрович")
        driver.find_element_by_name("content.policyHolder.dob").send_keys("01011990")
        driver.find_element_by_name("content.policyHolder.phone").send_keys("1231231212")
        driver.find_element(*TaxHelpLocators.InsurerMale).click()
        driver.find_element_by_name("content.policyHolder.email").send_keys("knikitin@avinfors.ru")
        driver.find_element_by_name("content.policyHolder.email2").send_keys("knikitin@avinfors.ru")
        driver.find_element_by_name("content.policyHolder.document.seria").send_keys("1234")
        driver.find_element_by_name("content.policyHolder.document.number").send_keys("123456")
        driver.find_element(*TaxHelpLocators.ButtonInsurerContinue).click()

    def insured_info(self):
        driver = self.driver
        driver.find_element_by_xpath("(//button[@type='button'])[6]").click()

    def agree(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@id='RI-product-steps']/div[4]/div/div/div/div/div/div/label").click()
        #driver.find_element_by_xpath("//div[@id='root']/div/div/div/div[2]").click()

    def fill_frame(self):
        self.conditions()
        self.insurer_info()
        self.insured_info()
        self.agree()

