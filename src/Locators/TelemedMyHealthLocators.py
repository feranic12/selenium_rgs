from selenium.webdriver.common.by import By


class TelemedMyHealthLocators:
    BuyButton = (By.CSS_SELECTOR, "div.table-responsive>table>tfoot td:nth-child(2)>button")
    InsurerLastName = (By.NAME, "content.policyHolder.lastName")
    InsurerFirstName = (By.NAME, "content.policyHolder.firstName")
    InsurerMiddleName = (By.NAME, "content.policyHolder.middleName")
    InsurerDob = (By.NAME, "content.policyHolder.dob")
    InsurerEMail = (By.NAME, "content.policyHolder.email")
    InsurerEMail2 = (By.NAME, "content.policyHolder.email2")
    InsurerPassportSeria = (By.NAME, "content.policyHolder.document.seria")
    InsurerMale = (By.CSS_SELECTOR,"div[data-name=\"content.policyHolder.sex\"] button:first-child")
    InsurerPhone = (By.NAME, "content.policyHolder.phone")
    InsurerPassportNumber = (By.NAME, "content.policyHolder.document.number")
    ContinueButton = (By.XPATH, "//div[@id='RI-product-steps']/div[2]/div/div[5]/button")