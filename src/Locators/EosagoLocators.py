from selenium.webdriver.common.by import By


class EosagoLocators:
    Capacity = (By.NAME, "content.object.data.power.value")
    Mark = (By.ID,"react-select-2-input")
    ProdYear = (By.NAME, "content.object.data.prodYear")
    Model = (By.ID, "react-select-3-input")
    VIN = (By.NAME, "content.object.data.vin")
    GosNumber = (By.NAME, "content.object.data.gosNumber")
    StsSeria = (By.NAME, "content.object.data.sts.seria")
    StsNumber = (By.NAME, "content.object.data.sts.number")
    StsDoi = (By.NAME, "content.object.data.sts.doi")
    ContinueButton = (By.CSS_SELECTOR, "div.text-right > button")