from selenium.webdriver.common.by import By


class TaxHelpLocators:
    BuyButton = (By.CSS_SELECTOR, "div.table-responsive td:nth-child(2)>button")
    InsurerMale = (By.CSS_SELECTOR, "div[data-name=\"content.policyHolder.sex\"] button:first-child")
    ButtonContinue = (By.CSS_SELECTOR, "div.clearfix>button")