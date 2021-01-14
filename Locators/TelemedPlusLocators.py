from selenium.webdriver.common.by import By


class TelemedPlusLocators:
    Button_Prolongation_False = (By.ID, "content.contract.data.prolongation.is-false")
    ButtonBuy1 = (By.XPATH, "//table//tr[9]/td[2]/button")
    Surname = (By.NAME, "content.policyHolder.lastName")
    First_Name = (By.NAME,"content.policyHolder.firstName")
    Middle_Name = (By.NAME,"content.policyHolder.middleName")
    DateOfBirth = (By.CSS_SELECTOR, "input[data-name=\"content.policyHolder.dob\"]")
    Phone = (By.NAME, "content.policyHolder.phone")
    Male = (By.ID, "content.policyHolder.sex-male")
    EMail1 = (By.NAME,"content.policyHolder.email")
    EMail2 = (By.NAME,"content.policyHolder.email2")
    Seria = (By.NAME, "content.policyHolder.document.seria")
    Number = (By.NAME, "content.policyHolder.document.number")
    Continue_Button2 = (By.CSS_SELECTOR, "div.text-right>button")
    Continue_Button3 = (By.CSS_SELECTOR, "div.text-right>button")
    Is_Insurer = (By.ID, "content.insuredPerson.is.type-policyHolder")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"]")