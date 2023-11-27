from selenium.webdriver.common.by import By


class HouseflatLocators:
    FlatButton = (By.CSS_SELECTOR, "div[data-name=\"content.object.data.type\"] button:first-child")
    BuildingYear = (By.NAME, "content.object.data.buildingYear")
    AddressNew1 = (By.NAME, "content.object.data.address.registration.city.full")
    AddressNew2 = (By.NAME, "content.object.data.address.registration.addressCdi.short")
    Flat = (By.NAME, "content.object.data.address.registration.flat")
    Cadastre = (By.NAME, "content.object.data.cadastreNumber")
    Program5 = (By.XPATH, ".//div[@class=\"table-responsive\"]//table//tr[4]/td[1]/button[1]")
    ContinueButton = (By.CSS_SELECTOR, "div.ml-auto > button")
    MaleButton = (By.CSS_SELECTOR, "div[data-name=\"content.policyHolder.sex\"] button:first-child")
    AddressSame = (By.CSS_SELECTOR, "label[for=\"content.policyHolder.address.registration.same_custom_input\"]")
    Accept = (By.CSS_SELECTOR, "label[for=\"content.temp.accept_custom_input\"]")
