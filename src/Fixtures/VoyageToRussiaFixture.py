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
from Locators.VoyageToRussiaLocators import VoyageToRussiaLocators


class VoyageToRussiaFixture(BaseFixture):
    def __init__(self, browser, lang):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-voyageToRussia.html"
        self.basic_setup(browser)
        self.lang = lang

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def switch_language(self):
        driver = self.driver
        if self.lang == "RUS":
            driver = self.driver
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(VoyageToRussiaLocators.LanguageSwitcher))
            element = driver.find_element(*VoyageToRussiaLocators.LanguageSwitcher)
            element.click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaLocators.Insured0Dob))
        else:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaLocators.Insured0Dob))

    def insured_birthdates(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaLocators.Insured0Dob))
        element = driver.find_element(*VoyageToRussiaLocators.Insured0Dob)
        element.send_keys("01011990")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaLocators.TripType))
        element = driver.find_element(*VoyageToRussiaLocators.TripType)
        element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaLocators.Coverage))
        element = driver.find_element(*VoyageToRussiaLocators.Coverage)
        element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaLocators.TripStart))
        element = driver.find_element(*VoyageToRussiaLocators.TripStart)
        element.send_keys(get_begin_day(6))
        element = driver.find_element(*VoyageToRussiaLocators.TripEnd)
        element.send_keys(get_begin_day(20))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaLocators.SportYes))
        element = driver.find_element(*VoyageToRussiaLocators.SportYes)
        element.click()
        element = driver.find_element(*VoyageToRussiaLocators.BuyEconom)
        element.click()

    def additional_coverage(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaLocators.NextButton1))
        element = driver.find_element(*VoyageToRussiaLocators.NextButton1)
        element.click()

    def insured_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaLocators.Insured0FirstName))
        element = driver.find_element(*VoyageToRussiaLocators.Insured0FirstName)
        element.send_keys("Ivan")
        element = driver.find_element(*VoyageToRussiaLocators.Insured0LastName)
        element.send_keys("Ivanov")
        element = driver.find_element(*VoyageToRussiaLocators.PassportSeria)
        element.send_keys("12")
        element = driver.find_element(*VoyageToRussiaLocators.PassportNumber)
        element.send_keys("123456")
        element = driver.find_element(*VoyageToRussiaLocators.NextButton1)
        element.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaLocators.InsurerFirstName))
        element = driver.find_element(*VoyageToRussiaLocators.InsurerFirstName)
        element.send_keys("Petr")
        element = driver.find_element(*VoyageToRussiaLocators.InsurerLastName)
        element.send_keys("Petrov")
        element = driver.find_element(*VoyageToRussiaLocators.InsurerDob)
        element.send_keys("01011980")
        element = driver.find_element(*VoyageToRussiaLocators.InsurerPhone)
        element.send_keys("123123213")
        element = driver.find_element(*VoyageToRussiaLocators.InsurerEmail)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*VoyageToRussiaLocators.InsurerEmail2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*VoyageToRussiaLocators.NextButton1)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaLocators.AcceptAllInput))
        element = driver.find_element(*VoyageToRussiaLocators.AcceptAllInput)
        element.click()

    def fill_frame(self):
        self.switch_language()
        self.insured_birthdates()
        self.conditions()
        self.additional_coverage()
        self.insured_info()
        self.insurer_info()
        self.agree()
