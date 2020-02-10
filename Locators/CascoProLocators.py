from selenium.webdriver.common.by import By

class CascoProLocators:
    ButtonBuy1 = (By.CSS_SELECTOR, "table tr:last-child>td:nth-child(2)>button")
    Mk = (By.ID, "react-select-2-input")
    Model = (By.ID, "react-select-3-input")
    Year_Of_Issue = (By.CLASS_NAME,"css-1hwfws3")