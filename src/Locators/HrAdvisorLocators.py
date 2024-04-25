from selenium.webdriver.common.by import By


class HrAdvisorLocators:
    PolicySeria = (By.NAME, "content.contract.data.policy.seria")
    PolicyNumber = (By.NAME, "content.contract.data.policy.number")
    ActivationCode = (By.NAME, "content.contract.data.activationCode")
    IssueDate = (By.NAME, "content.contract.issueDate")
    PolicyHolderLastName = (By.NAME, "content.policyHolder.lastName")
    PolicyHolderFirstName = (By.NAME, "content.policyHolder.firstName")
    PolicyHolderMiddleName = (By.NAME, "content.policyHolder.middleName")
    PolicyHolderDob = (By.NAME, "content.policyHolder.dob")
    PolicyHolderPhone = (By.NAME, "content.policyHolder.phone")
    PolicyHolderEmail = (By.NAME, "content.policyHolder.email")
    InsuredPersonLastName = (By.NAME, "content.insuredPerson.lastName")
    InsuredPersonFirstName = (By.NAME, "content.insuredPerson.firstName")
    InsuredPersonMiddleName = (By.NAME, "content.insuredPerson.middleName")
    InsuredPersonDob = (By.NAME, "content.insuredPerson.dob")
    InsuredPersonSex = (By.CSS_SELECTOR, "div[data-name=\"content.insuredPerson.sex\"] button:first-child")
    InsuredPersonPhone = (By.NAME, "content.insuredPerson.phone")
    InsuredPersonEmail = (By.NAME, "content.insuredPerson.email")
    AcceptAllInput = (By.CSS_SELECTOR, "label[for=\"properties.accept_custom_input\"]")