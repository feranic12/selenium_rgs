from config import chromedriver_path, chrome_binary_path, geckodriver_path, firefox_binary_path
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
    def __init__(self, browser, target):
        chrome_options = ChromeOptions()
        self.target = target
        if browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
        elif browser == "firefox":
            self.driver = webdriver.Firefox(executable_path=geckodriver_path)
        self.actions = action_chains.ActionChains(self.driver)

    def open_page(self):
        self.driver.get(self.target)

    def destroy(self):
        self.driver.quit()