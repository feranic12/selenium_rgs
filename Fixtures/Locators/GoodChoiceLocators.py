from selenium.webdriver.common.by import By


class GoodChoiceLocators:
    Button1 = (By.CSS_SELECTOR, "div.mt-3 tr:last-child>td:nth-child(2)>button")
    Button_Flat = (By.ID, "content.object.data.type-flat")
    Region_Input = (By.ID,"react-select-2-input")
    City = (By.ID, "content-object-data-address-registration-city-name")
    Street = (By.ID, "content-object-data-address-registration-street-name")
    House = (By.ID,"content-object-data-address-registration-house")
    Corp = (By.ID, "content-object-data-address-registration-corp")
    Building = (By.ID, "content-object-data-address-registration-building")
    Flat = (By.ID, "content-object-data-address-registration-flat")
    Continue_Button1 = (By.CSS_SELECTOR, "div.text-right>button")
    