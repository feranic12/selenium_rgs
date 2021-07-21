from selenium.webdriver.common.by import By


class TelemedMyHealthLocators:
    BuyButton = (By.CSS_SELECTOR, "div.table-responsive>table>tfoot td:nth-child(2)>button")
    InsurerLastName = (By.NAME, "content.policyHolder.lastName")
    InsurerFirstName = (By.NAME, "content.policyHolder.firstName")
    InsurerMiddleName = (By.NAME, "content.policyHolder.middleName")
    InsurerMale = (By.XPATH, "//div[@id='RI-product-steps']/div[2]/div/div[2]/div[5]/div/div/div/div/button")
    InsurerPhone = (By.NAME, "content.policyHolder.phone")
    InsurerEMail = (By.NAME, "content.policyHolder.email")
    InsurerEMail2 = (By.NAME, "content.policyHolder.email2")
    InsurerPassportSeria = (By.NAME, "content.policyHolder.document.seria")
    InsurerPassportNumber = (By.NAME, "content.policyHolder.document.number")
    ContinueButton = (By.XPATH, "//div[@id='RI-product-steps']/div[2]/div/div[5]/button")