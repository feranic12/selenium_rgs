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
from Locators.HomeProtectLocators import HomeProtectLocators


class HomeProtectFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-homeProtect.html"
        self.basic_setup(browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomeProtectLocators.BuyButton))
        driver.find_element(*HomeProtectLocators.BuyButton).click()

    def insurance_object(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomeProtectLocators.AddressCDI))
        element = driver.find_element(*HomeProtectLocators.AddressCDI)
        element.send_keys("г Москва, г Зеленоград, пл Юности, д 1")
        time.sleep(1)
        element.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element(*HomeProtectLocators.ButtonContinue).click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "content.policyHolder.firstName")))
        driver.find_element_by_name("content.policyHolder.lastName").send_keys(u"Петров")
        driver.find_element_by_name("content.policyHolder.firstName").send_keys(u"Петр")
        driver.find_element_by_name("content.policyHolder.middleName").send_keys(u"Петрович")
        driver.find_element_by_name("content.policyHolder.dob").send_keys("01011990")
        driver.find_element_by_name("content.policyHolder.phone").send_keys("1231231212")
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_name("content.policyHolder.email").send_keys("knikitin@avinfors.ru")
        driver.find_element_by_name("content.policyHolder.email2").send_keys("knikitin@avinfors.ru")
        driver.find_element_by_xpath("//div[@id='RI-product-steps']/div[3]/div/div[2]/div[2]/div").click()
        driver.find_element_by_name("content.policyHolder.document.seria").send_keys("1234")
        driver.find_element_by_xpath("//div[@id='RI-product-steps']/div[3]/div/div[2]/div[3]/div").click()
        driver.find_element_by_name("content.policyHolder.document.number").send_keys("123123")
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(HomeProtectLocators.AcceptAllInput))
        driver.find_element(*HomeProtectLocators.AcceptAllInput).click()

    def fill_frame(self):
        self.conditions()
        self.insurance_object()
        self.insurer_info()
        self.agree()