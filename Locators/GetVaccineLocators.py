from selenium.webdriver.common.by import By

class GetVaccineLocators:
    ButtonBuy = (By.CSS_SELECTOR, "table.Table_table__Ivg85 tr:last-child button")
    IsInsured = (By.CSS_SELECTOR, "label[for=\"content.insuredPerson.is.type_custom_input\"]")
    InsurersLastname = (By.NAME, "content.policyHolder.lastName")
    InsurersFirstname = (By.NAME, "content.policyHolder.firstName")
    InsurersMiddlename = (By.NAME, "content.policyHolder.middleName")
    InsurersDob = (By.CSS_SELECTOR, "input[data-name=\"content.policyHolder.dob\"]")
    InsurersPhone = (By.NAME, "content.policyHolder.phone")
    InsurerMale = (By.ID, "content.policyHolder.sex-male")
    InsurersEmail = (By.NAME, "content.policyHolder.email")
    InsurersEmail2 = (By.NAME, "content.policyHolder.email2")
    InsurersPassportSeria = (By.NAME, "content.policyHolder.document.seria")
    InsurersPassportNumber = (By.NAME, "content.policyHolder.document.number")
    ContinueButton = (By.CSS_SELECTOR, "div.text-right > button")
    AcceptAllInput = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"]")