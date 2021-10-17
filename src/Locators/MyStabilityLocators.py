from selenium.webdriver.common.by import By


class MyStabilityLocators:
    BuyButton = (By.CSS_SELECTOR, "td.text-right > button")
    MaleButton = (By.CSS_SELECTOR, "div[data-name=\"content.policyHolder.sex\"] button:first-child")
    ContinueButton = (By.CSS_SELECTOR, "div.ml-auto > button")
    Accept1 = (By.CSS_SELECTOR, "label[for=\"accept1\"]::before")
    Accept2 = (By.CSS_SELECTOR, "label[for=\"accept2\"]")
