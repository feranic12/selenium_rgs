from selenium.webdriver.common.by import By


class VoyageToRussiaCommonLocators:
    Insured0Dob = (By.NAME, "content.insConditions.insVariant.insurersDob[0].dob")
    TripType = (By.CSS_SELECTOR, "div[data-name=\"content.insConditions.insVariant.tripType\"] button:first-child")
    Coverage = (By.CSS_SELECTOR, "div[data-name=\"content.insConditions.insVariant.risks.medical.limit\"] button:first-child")
    TripStart = (By.NAME, "content.contract.beginDate")
    TripEnd = (By.NAME, "content.contract.endDate")
    SportYes = (By.CSS_SELECTOR, "div[data-name=\"content.insConditions.insVariant.risks.sport.on\"] button:first-child")
    BuyEconom = (By.CSS_SELECTOR,"div.table-responsive tr:last-child>td:nth-child(2)")
    NextButton1 = (By.CSS_SELECTOR, "div.text-right > button")
    Insured0FirstName = (By.NAME, "content.insConditions.insVariant.insurersDob[0].firstName")
    Insured0LastName = (By.NAME, "content.insConditions.insVariant.insurersDob[0].lastName")
    PassportSeria = (By.NAME,"content.insConditions.insVariant.insurersDob[0].document.seria")
    PassportNumber = (By.NAME,"content.insConditions.insVariant.insurersDob[0].document.number")
    InsurerFirstName = (By.NAME, "content.policyHolder.firstName")
    InsurerLastName = (By.NAME, "content.policyHolder.lastName")
    InsurerDob = (By.NAME, "content.policyHolder.dob")
    InsurerPhone = (By.NAME, "content.policyHolder.phone")
    InsurerEmail = (By.NAME, "content.policyHolder.email")
    InsurerEmail2 = (By.NAME, "content.policyHolder.email2")
    AcceptAllInput = (By.CSS_SELECTOR, "label[for=\"content.temp.accept1_custom_input")