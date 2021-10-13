from selenium.webdriver.common.by import By


class HouseflatLocators:
    FlatButton = (By.CSS_SELECTOR, "div[data-name=\"content.object.data.type\"] button:first-child")
    AddressCDI = (By.CSS_SELECTOR, "input[data-name=\"content.object.data.address.registration.addressCdi\"]")
    Flat = (By.NAME, "content.object.data.address.registration.flat")
    Cadastre = (By.NAME, "content.object.data.cadastreNumber")
    Program5 = (By.XPATH, ".//div[@class=\"table-responsive\"]//table//tr[4]/td[2]/button[1]")
    ContinueButton = (By.CSS_SELECTOR, "div.ml-auto > button")
