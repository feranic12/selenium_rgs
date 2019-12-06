from selenium.webdriver.common.by import By


class RodnyeStenyLocators:
    Area_Input = (By.ID, "content-object-data-area")
    Region_Button = (By.ID,"content.object.data.flatbaseRegion-1")
    Owned_Button = (By.ID, "content.object.data.privat-yes")
    Rent_Button = (By.ID, "content.object.data.rent-yes")
    Fire_Button = (By.ID, "content.object.data.fire-yes")
    Buy_Premium_Button = (By.CSS_SELECTOR, "div.card-group > div:nth-child(3) button")
    Begin_Date_Input = (By.ID, "content-contract-beginDate")
    Region_Input = (By.ID, "react-select-5-input")