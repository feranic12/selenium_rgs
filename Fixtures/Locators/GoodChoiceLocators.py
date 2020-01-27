from selenium.webdriver.common.by import By


class GoodChoiceLocators:
    Button1 = (By.CSS_SELECTOR, "div.mt-3 tr:last-child>td:nth-child(2)>button")
    Button_Flat = (By.ID, "content.object.data.type-flat")
    Region_Input = (By.ID,"react-select-2-input")