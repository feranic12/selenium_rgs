from selenium.webdriver.common.by import By


class MainPageLocators:
    Insurers0_Dob_Input = (By.ID, "insuredPerson-0-dob")
    Trip_Type_Button = (By.ID, "content.insConditions.insVariant.tripType-single")
    Country_Input = (By.ID, "content-insConditions-insVariant-countries")
