from selenium.webdriver.common.by import By

class HomeProtectLocators:
    BuyButton = (By.CSS_SELECTOR, "div.table-responsive td:nth-child(2)>button")
    AddressCDI = (By.CSS_SELECTOR, "input[data-name=\"content.object.data.address.registration.addressCdi\"]")
    Male = (By.CSS_SELECTOR, "div[data-name=\"content.policyHolder.sex\"] button:first-child")
    ButtonContinue = (By.CSS_SELECTOR, "div.clearfix > button")
    AcceptAllInput = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"]")
