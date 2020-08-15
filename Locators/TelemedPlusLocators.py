from selenium.webdriver.common.by import By


class TelemedPlusLocators:
    ButtonBuy1 = (By.XPATH, "//table//tr[9]/td[2]/button")
    Surname = (By.ID, "content-policyHolder-lastName")
    First_Name = (By.ID,"content-policyHolder-firstName")
    Middle_Name = (By.ID,"content-policyHolder-middleName")
    DateOfBirth = (By.ID, "content-policyHolder-dob")
    Phone = (By.ID, "content-policyHolder-phone")
    Male = (By.ID, "content.policyHolder.sex-male")
    EMail1 = (By.ID,"content-policyHolder-email")
    EMail2 = (By.ID,"content-policyHolder-email2")
    Seria = (By.ID, "content-policyHolder-document-seria")
    Number = (By.ID, "content-policyHolder-document-number")
    Continue1 = (By.CSS_SELECTOR, "div.text-right>button")
    Continue2 = (By.CSS_SELECTOR, "div.text-right>button")
    Is_Insurer = (By.ID, "content.insuredPerson.is.type-policyHolder")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"]")