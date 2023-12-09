from selenium.webdriver.common.by import By


class CardProtectLocators:
    End_Date = (By.NAME, "content.object.data.endDate")
    Buy_Button = (By.XPATH, "//div[@class='table-responsive']//tr[6]/td[2]//button")
    Male = (By.CSS_SELECTOR, "div[data-name='content.policyHolder.sex']")
    Continue_Button = (By.CSS_SELECTOR, "button[type='submit']")
    Accept = (By.CSS_SELECTOR, "label[for='accept']")