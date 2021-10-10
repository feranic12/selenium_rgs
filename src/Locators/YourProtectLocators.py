from selenium.webdriver.common.by import By


class YourProtectLocators:
    Sport_Yes = (By.CSS_SELECTOR, "div[data-name=\"content.insConditions.insVariant.sport\"] button:first-child ")
    Term_Months_3 = (By.CSS_SELECTOR, "div[data-name=\"content.insConditions.insVariant.termMonths\"] button:nth-child(2)")
    Continue_Button_1= (By.CSS_SELECTOR, "div.ml-auto > button")
    Sports_Checkbox = (By.CSS_SELECTOR, "label[for=\"content.insConditions.insVariant.sportListSame_custom_input\"]")