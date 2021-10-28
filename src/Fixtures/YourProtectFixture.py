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
from Locators.YourProtectLocators import YourProtectLocators
from utils import get_begin_day


class YourProtectFixture(BaseFixture):
    def __init__(self, browser):
        self.target = r"https://testpartner.rgs.ru/b2c/product/build/test-yourProtect.html"
        BaseFixture.__init__(self, browser)

    def open_page(self):
        BaseFixture.open_page(self)
        self.driver.switch_to.frame("RESOLUTE_INSURANCE")

    def conditions(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(YourProtectLocators.Sport_Yes))
        driver.find_element(*YourProtectLocators.Sport_Yes).click()
        driver.find_element(*YourProtectLocators.Term_Months_3).click()
        driver.find_element(*YourProtectLocators.Continue_Button).click()

    def insured_info(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(YourProtectLocators.Sports_Checkbox))
        driver.find_element(*YourProtectLocators.Sports_Checkbox).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "content.insConditions.insVariant.sportList.data")))
        driver.find_element_by_id("content.insConditions.insVariant.sportList.data").send_keys("Теннис(настольный)" + Keys.ENTER)
        driver.find_element(By.NAME, "content.insuredPerson.list[0].lastName").send_keys("Петров")
        driver.find_element(By.NAME, "content.insuredPerson.list[0].firstName").send_keys("Пётр")
        driver.find_element(By.NAME, "content.insuredPerson.list[0].middleName").send_keys("Петрович")
        driver.find_element(By.NAME, "content.insuredPerson.list[0].dob").send_keys("01011990")
        driver.find_element(By.NAME, "content.insuredPerson.list[0].phone").send_keys("1231231212")
        driver.find_element(*YourProtectLocators.Male).click()
        driver.find_element(*YourProtectLocators.IsInsurer).click()
        driver.find_element(*YourProtectLocators.DMS).click()
        driver.find_element(*YourProtectLocators.Mite).click()
        driver.find_element(*YourProtectLocators.Continue_Button).click()

    def insurer_info(self):
        driver = self.driver
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME, "content.policyHolder.email")))
        driver.find_element(By.NAME, "content.policyHolder.email").send_keys("knikitin@avinfors.ru")
        driver.find_element(By.NAME, "content.policyHolder.email2").send_keys("knikitin@avinfors.ru")
        driver.find_element(*YourProtectLocators.Continue_Button).click()

    def agree(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(YourProtectLocators.Accept))
        driver.find_element(*YourProtectLocators.Accept).click()

    def fill_frame(self):
        self.conditions()
        self.insured_info()
        self.insurer_info()
        self.agree()