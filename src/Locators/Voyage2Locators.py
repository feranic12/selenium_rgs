from selenium.webdriver.common.by import By


class Voyage2Locators:
    Dob1 = (By.NAME, "content.insuredPerson.list[0].dob")
    OneTimeButton = (By.CSS_SELECTOR, "div[data-name=\"content.insConditions.insVariant.tripType\"] button:first-child")
    Countries = (By.ID, "react-select-2-input")
    InsSum = (By.CSS_SELECTOR, "div[data-name=\"content.insConditions.insVariant.covers.medical.limit\"] button:nth-child(2)")
    BeginDate = (By.NAME, "content.contract.beginDate")
    EndDate = (By.NAME, "content.contract.arrival")
    SportYes = (By.CSS_SELECTOR, "div[data-name=\"content.insConditions.insVariant.options.sportK\"] button:first-child")
    BuyPremium = (By.CSS_SELECTOR, "div.mt-2 tr:last-child>td:last-child>button")
    ContinueWithout = (By.CSS_SELECTOR, "div.text-right button")
    Insured0LastName = (By.NAME, "content.insuredPerson.list[0].lastName")
    Insured0FirstName = (By.NAME, "content.insuredPerson.list[0].firstName")
    Insured0MiddleName = (By.NAME, "content.insuredPerson.list[0].middleName")
    Continue1 = (By.CSS_SELECTOR, "div.text-right button")
    InsurerLastName = (By.NAME, "content.policyHolder.lastName")
    InsurerFirstName = (By.NAME, "content.policyHolder.firstName")
    InsurerMiddleName = (By.NAME, "content.policyHolder.middleName")
    InsurerDob = (By.NAME, "content.policyHolder.dob")
    InsurerPhone = (By.NAME, "content.policyHolder.phone")
    InsurerEmail = (By.NAME, "content.policyHolder.email")
    InsurerEmail2 = (By.NAME, "content.policyHolder.email2")
    InsurerPassportSeria = (By.NAME, "content.policyHolder.document.seria")
    InsurerPassportNumber = (By.NAME, "content.policyHolder.document.number")
    Continue2 = (By.CSS_SELECTOR, "div.text-right button")
    Accept = (By.CSS_SELECTOR, "label[for=\"content.temp.accept1_custom_input\"]")

