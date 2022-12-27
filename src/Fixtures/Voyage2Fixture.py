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
from Locators.Voyage2Locators import Voyage2Locators


class Voyage2Fixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://test2partner.rgs.ru/b2c/product/build/test-voyage2.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Voyage2Locators.Dob1))
        element = driver.find_element(*Voyage2Locators.Dob1)
        element.send_keys("01012021")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Voyage2Locators.OneTimeButton))
        element = driver.find_element(*Voyage2Locators.OneTimeButton)
        element.click()
        element = driver.find_element(*Voyage2Locators.Countries)
        element.send_keys("Австрия" + Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Voyage2Locators.InsSum))
        element = driver.find_element(*Voyage2Locators.InsSum)
        element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Voyage2Locators.BeginDate))
        element = driver.find_element(*Voyage2Locators.BeginDate)
        element.send_keys(get_begin_day(10))
        element = driver.find_element(*Voyage2Locators.EndDate)
        element.send_keys(get_begin_day(20))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Voyage2Locators.SportYes))
        element = driver.find_element(*Voyage2Locators.SportYes)
        element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Voyage2Locators.BuyPremium))
        element = driver.find_element(*Voyage2Locators.BuyPremium)
        element.click()

    def additional_conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Voyage2Locators.ContinueWithout))
        element = driver.find_element(*Voyage2Locators.ContinueWithout)
        element.click()

    def insured0_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Voyage2Locators.Insured0LastName))
        element = driver.find_element(*Voyage2Locators.Insured0LastName)
        element.send_keys("Petrov")
        element = driver.find_element(*Voyage2Locators.Insured0FirstName)
        element.send_keys("Petr")
        element = driver.find_element(*Voyage2Locators.Continue1)
        element.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Voyage2Locators.InsurerLastName))
        element = driver.find_element(*Voyage2Locators.InsurerLastName)
        element.send_keys("Иванов")
        element = driver.find_element(*Voyage2Locators.InsurerFirstName)
        element.send_keys("Иван")
        element = driver.find_element(*Voyage2Locators.InsurerMiddleName)
        element.send_keys("Иванович")
        element = driver.find_element(*Voyage2Locators.InsurerDob)
        element.send_keys("01011990")
        element = driver.find_element(*Voyage2Locators.InsurerPhone)
        element.send_keys("1231231212")
        element = driver.find_element(*Voyage2Locators.InsurerEmail)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*Voyage2Locators.InsurerEmail2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*Voyage2Locators.Continue2)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Voyage2Locators.Accept))
        element = driver.find_element(*Voyage2Locators.Accept)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.additional_conditions()
        self.insured0_info()
        self.insurer_info()
        self.agree()
