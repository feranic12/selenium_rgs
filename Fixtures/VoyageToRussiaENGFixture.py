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
from Fixtures.VoyageToRussiaFixture import VoyageToRussiaFixture
from Locators.VoyageToRussiaCommonLocators import VoyageToRussiaCommonLocators
from abc import ABC, abstractmethod


class VoyageToRussiaENGFixture(VoyageToRussiaFixture, ABC):
    def __init__(self, browser):
        VoyageToRussiaFixture.__init__(self, browser)

    def open_page(self):
        VoyageToRussiaFixture.open_page(self)

    def insured_birthdates(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaCommonLocators.Insured0Dob))
        element = driver.find_element(*VoyageToRussiaCommonLocators.Insured0Dob)
        element.send_keys("01011990")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaCommonLocators.TripType))
        element = driver.find_element(*VoyageToRussiaCommonLocators.TripType)
        element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaCommonLocators.Coverage))
        element = driver.find_element(*VoyageToRussiaCommonLocators.Coverage)
        element.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaCommonLocators.TripStart))
        element = driver.find_element(*VoyageToRussiaCommonLocators.TripStart)
        element.send_keys(get_begin_day(6))
        element = driver.find_element(*VoyageToRussiaCommonLocators.TripEnd)
        element.send_keys(get_begin_day(20))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaCommonLocators.SportYes))
        element = driver.find_element(*VoyageToRussiaCommonLocators.SportYes)
        element.click()
        element = driver.find_element(*VoyageToRussiaCommonLocators.BuyEconom)
        element.click()

    def additional_coverage(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaCommonLocators.NextButton1))
        element = driver.find_element(*VoyageToRussiaCommonLocators.NextButton1)
        element.click()

    def insured_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaCommonLocators.Insured0FirstName))
        element = driver.find_element(*VoyageToRussiaCommonLocators.Insured0FirstName)
        element.send_keys("Ivan")
        element = driver.find_element(*VoyageToRussiaCommonLocators.Insured0LastName)
        element.send_keys("Ivanov")
        element = driver.find_element(*VoyageToRussiaCommonLocators.PassportSeria)
        element.send_keys("12")
        element = driver.find_element(*VoyageToRussiaCommonLocators.PassportNumber)
        element.send_keys("123456")
        element = driver.find_element(*VoyageToRussiaCommonLocators.NextButton1)
        element.click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaCommonLocators.InsurerFirstName))
        element = driver.find_element(*VoyageToRussiaCommonLocators.InsurerFirstName)
        element.send_keys("Petr")
        element = driver.find_element(*VoyageToRussiaCommonLocators.InsurerLastName)
        element.send_keys("Petrov")
        element = driver.find_element(*VoyageToRussiaCommonLocators.InsurerDob)
        element.send_keys("01011980")
        element = driver.find_element(*VoyageToRussiaCommonLocators.InsurerPhone)
        element.send_keys("123123213")
        element = driver.find_element(*VoyageToRussiaCommonLocators.InsurerEmail)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*VoyageToRussiaCommonLocators.InsurerEmail2)
        element.send_keys("knikitin@avinfors.ru")
        element = driver.find_element(*VoyageToRussiaCommonLocators.NextButton1)
        element.click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(VoyageToRussiaCommonLocators.AcceptAllInput))
        element = driver.find_element(*VoyageToRussiaCommonLocators.AcceptAllInput)
        element.click()