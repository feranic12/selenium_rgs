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
from abc import ABC, abstractmethod


class VoyageToRussiaFixture(BaseFixture, ABC):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-voyageToRussia.html"
        self.basic_setup(browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    @abstractmethod
    def insured_birthdates(self):
        pass

    @abstractmethod
    def conditions(self):
        pass

    @abstractmethod
    def additional_coverage(self):
        pass

    @abstractmethod
    def insured_info(self):
        pass

    @abstractmethod
    def insurer_info(self):
        pass

    @abstractmethod
    def agree(self):
        pass

    def fill_frame(self):
        self.insured_birthdates()
        self.conditions()
        self.additional_coverage()
        self.insured_info()
        self.insurer_info()
        self.agree()


