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
from Fixtures.Locators.GoodChoiceLocators import GoodChoiceLocators


class GoodChoiceFixture:
    def __init__(self, browser):
        target = r"https://avinfors.ru/denis_rgs2/b2c/product/build/test-goodChoiceB2B.html"
        BaseFixture.__init__(self, browser, target)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        element = driver.find_element(*GoodChoiceLocators.Button1)
        element.click()

    def insurance_object(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(GoodChoiceLocators.Button_Flat))
        element = driver.find_element(*GoodChoiceLocators.Button_Flat)
        element.click()
        element = driver.find_element(*GoodChoiceLocators.Region_Input)
        element.send_keys("город.Москва" + Keys.ENTER)
        element = driver.find_element(*GoodChoiceLocators.City)
        element.send_keys("Москва")
        element = driver.find_element(*GoodChoiceLocators.Street)
        element.send_keys("ул.Ленина")
        element = driver.find_element(*GoodChoiceLocators.House)
        element.send_keys("12")
        element = driver.find_element(*GoodChoiceLocators.Corp)
        element.send_keys("13")
        element = driver.find_element(*GoodChoiceLocators.Building)
        element.send_keys("14")
        element = driver.find_element(*GoodChoiceLocators.Flat)
        element.send_keys("15")
        element = driver.find_element(*GoodChoiceLocators.Continue_Button1)
        element.click()

    def fill_frame(self):
        self.conditions()
        self.insurance_object()