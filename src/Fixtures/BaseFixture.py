import config
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time


class BaseFixture:
    def basic_setup(self, browser):
        if browser == "chrome":
            chrome_options = ChromeOptions()
            self.driver = webdriver.Chrome(executable_path=config.chromedriver_path, options=chrome_options)
        elif browser == "firefox":
            self.driver = webdriver.Firefox(executable_path=config.geckodriver_path)
        elif browser == "ie":
            self.driver = webdriver.Ie(executable_path=config.iedriver_path)
        elif browser == "opera":
            self.driver = webdriver.Opera(executable_path=config.operadriver_path)
        self.driver.implicitly_wait(30)
        self.actions = action_chains.ActionChains(self.driver)

    def open_page(self):
        self.driver.get(self.target)

    def destroy(self):
        self.driver.quit()