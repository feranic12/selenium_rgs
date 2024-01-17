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
from Locators.MyPetsLocators import MyPetsLocators


class MyPetsFixture:
    def __init__(self, browser):
        self.target = r"https://test2partner.rgs.ru/b2c/product/build/test-myPets.html?p=rgs"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MyPetsLocators.ButtonBuy1))
        driver.find_element(*MyPetsLocators.BeginDate).send_keys(get_begin_day(1))
        driver.find_element(*MyPetsLocators.ButtonBuy1).click()

    def calculation(self):
        driver = self.driver


    def fill_frame(self):
        self.conditions()
        self.calculation()