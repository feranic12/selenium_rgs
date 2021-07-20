from selenium.webdriver.common.by import By


class MyHealthPlusB2BLocators:
    BuyButton = (By.CSS_SELECTOR, "table.mt-3 td:nth-child(3) > button")
    InsurerLastname = (By.NAME, "content.policyHolder.lastName")
    InsurerFirstname = (By.NAME, "content.policyHolder.firstName")
    InsurerMiddlename = (By.NAME, "content.policyHolder.middleName")
    InsurerDob = (By.NAME, "content.policyHolder.dob")
    InsurerPhone = (By.NAME, "content.policyHolder.phone")
    MaleButton = (By.CSS_SELECTOR, "div[data-name=\"content.policyHolder.sex\"] button:first-child")
    Email = (By.NAME, "content.policyHolder.email")
    Email2 = (By.NAME, "content.policyHolder.email2")
    PassportSeria = (By.NAME, "content.policyHolder.document.seria")
    PassportNumber = (By.NAME, "content.policyHolder.document.number")
    ContinueButton = (By.CSS_SELECTOR, "div.clearfix > button")
    Accept = (By.CSS_SELECTOR, "label[for=\"content.temp.accept_custom_inputcontent.temp.accept\"}::after")