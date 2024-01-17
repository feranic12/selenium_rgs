from selenium.webdriver.common.by import By


class MyPetsLocators:
    ButtonBuy1 = (By.CSS_SELECTOR, "div.table-responsive tr:last-child > td:nth-child(2) button")
    BeginDate = (By.NAME, "content.contract.beginDate")
    PetType = (By.ID, )

