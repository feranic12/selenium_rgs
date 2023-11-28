from selenium.webdriver.common.by import By


class SafeRestLocators:
    InsuredDob = (By.NAME, "content.insuredPerson.list[0].dob")
    Term = (By.NAME, "content.insConditions.insVariant.term")
    MiteRisk = (By.CSS_SELECTOR, "label[for=\"content.insConditions.insVariant.risks.mite_custom_input\"]")
    MedicalRisk = (By.CSS_SELECTOR, "label[for=\"content.insConditions.insVariant.risks.medical_custom_input\"]")
    AccidentRisk = (By.CSS_SELECTOR, "label[for=\"content.insConditions.insVariant.risks.accident_custom_input\"]")
    SportOption = (By.CSS_SELECTOR, "label[for=\"content.insConditions.insVariant.options.sport_custom_input\"]")
    AlcOption = (By.CSS_SELECTOR, "label[for=\"content.insConditions.insVariant.options.alc_custom_input\"]")
    IllOption = (By.CSS_SELECTOR, "label[for=\"content.insConditions.insVariant.options.ill_custom_input\"]")
    ContinueButton = (By.CSS_SELECTOR, "button[type=\"submit\"]")
    Insured0LastName = (By.NAME, "content.insuredPerson.list[0].lastName")
    Insured0FirstName = (By.NAME, "content.insuredPerson.list[0].firstName")
    Insured0MiddleName = (By.NAME, "content.insuredPerson.list[0].middleName")
    InsurersPhone = (By.NAME, "content.policyHolder.phone")
    InsurersMale = (By.CSS_SELECTOR, "div[data-name=\"content.policyHolder.sex\"] button:first-child")
    InsurersEmail = (By.NAME, "content.policyHolder.email")
    InsurersEmail2= (By.NAME, "content.policyHolder.email2")
    Agree = (By.CSS_SELECTOR, "label[for=\"accept\"]")


