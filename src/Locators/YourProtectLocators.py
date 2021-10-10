from selenium.webdriver.common.by import By


class YourProtectLocators:
    Sport_Yes = (By.CSS_SELECTOR, "div[data-name=\"content.insConditions.insVariant.sport\"] button:first-child ")
    Term_Months_3 = (By.CSS_SELECTOR, "div[data-name=\"content.insConditions.insVariant.termMonths\"] button:nth-child(2)")
    Continue_Button= (By.CSS_SELECTOR, "div.ml-auto > button")
    Sports_Checkbox = (By.CSS_SELECTOR, "label[for=\"content.insConditions.insVariant.sportListSame_custom_input\"]")
    Male = (By.CSS_SELECTOR, "div[data-name=\"content.insuredPerson.list[0].sex\"] button:first-child")
    IsInsurer = (By.CSS_SELECTOR, "label[for=\"content.insuredPerson.list[0].data.policyHolder_custom_input\"]")
    DMS = (By.CSS_SELECTOR, "label[for=\"content.insConditions.insVariant.additionals.medical_custom_input\"]")
    Mite = (By.CSS_SELECTOR, "label[for=\"content.insConditions.insVariant.additionals.mite_custom_input\"]")
    Accept = (By.CSS_SELECTOR, "label[for=\"content.temp.accept_custom_input\"]")