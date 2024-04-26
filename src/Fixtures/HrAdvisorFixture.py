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
from datetime import datetime as dt
from datetime import timedelta
from Fixtures.BaseFixture import BaseFixture
from Locators.HrAdvisorLocators import HrAdvisorLocators


class HrAdvisorFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://test2partner.rgs.ru/b2c/box/build/test-hrAdvisor.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))

    def policy_info(self):
        driver = self.driver
        five_days_ago = dt.now() - timedelta(5)
        this_year = dt.now().strftime("%y")
        driver.find_element(*HrAdvisorLocators.PolicySeria).send_keys("IB903")
        driver.find_element(*HrAdvisorLocators.PolicyNumber).send_keys("1111222" + this_year)
        driver.find_element(*HrAdvisorLocators.ActivationCode).send_keys("1234")
        driver.find_element(*HrAdvisorLocators.IssueDate).send_keys(five_days_ago.strftime('%d%m%Y'))

    def insurer_info(self):
        driver = self.driver
        driver.find_element(*HrAdvisorLocators.PolicyHolderLastName).send_keys("Петров")
        driver.find_element(*HrAdvisorLocators.PolicyHolderFirstName).send_keys("Пётр")
        driver.find_element(*HrAdvisorLocators.PolicyHolderMiddleName).send_keys("Петрович")
        driver.find_element(*HrAdvisorLocators.PolicyHolderDob).send_keys("01011990")
        driver.find_element(*HrAdvisorLocators.PolicyHolderPhone).send_keys("1231231212")
        driver.find_element(*HrAdvisorLocators.PolicyHolderEmail).send_keys("knikitin@avinfors.ru")

    def insured_info(self):
        driver = self.driver
        driver.find_element(*HrAdvisorLocators.InsuredPersonLastName).send_keys("Иванов")
        driver.find_element(*HrAdvisorLocators.InsuredPersonFirstName).send_keys("Иван")
        driver.find_element(*HrAdvisorLocators.InsuredPersonMiddleName).send_keys("Иванович")
        driver.find_element(*HrAdvisorLocators.InsuredPersonDob).send_keys("01011990")
        driver.find_element(*HrAdvisorLocators.InsuredPersonPhone).send_keys("1231231212")
        driver.find_element(*HrAdvisorLocators.InsuredPersonSex).click()
        driver.find_element(*HrAdvisorLocators.InsuredPersonEmail).send_keys("knikitin@avinfors.ru")

    def agree(self):
        driver = self.driver
        driver.find_element(*HrAdvisorLocators.AcceptAllInput).click()

    def fill_frame(self):
        self.policy_info()
        self.insurer_info()
        self.insured_info()
        self.agree()