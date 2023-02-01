from selenium.webdriver.common.by import By


class TelemedPlusB2BLocators:
    Button_Prolongation_False = (By.CSS_SELECTOR, "div[data-name=\"content.contract.data.prolongation.is\"] button:first-child")
    #ButtonBuy1 = (By.XPATH, "//table//tr[9]/td[2]/button")
    ButtonBuy1 = (By.CSS_SELECTOR, "div.h-100 > div:last-child > button")
    Surname = (By.NAME, "content.policyHolder.lastName")
    First_Name = (By.NAME,"content.policyHolder.firstName")
    Middle_Name = (By.NAME,"content.policyHolder.middleName")
    DateOfBirth = (By.NAME, "content.policyHolder.dob")
    Phone = (By.NAME, "content.policyHolder.phone")
    Male = (By.CSS_SELECTOR, "div[data-name=\"content.policyHolder.sex\"] button:first-child")
    EMail1 = (By.NAME,"content.policyHolder.email")
    EMail2 = (By.NAME,"content.policyHolder.email2")
    Seria = (By.NAME, "content.policyHolder.document.seria")
    Number = (By.NAME, "content.policyHolder.document.number")
    Continue_Button2 = (By.CSS_SELECTOR, "div.text-right>button")
    Continue_Button3 = (By.CSS_SELECTOR, "div.text-right>button")
    Is_Insurer = (By.CSS_SELECTOR, "div[data-name=\"content.insuredPerson.is.type\"] button:first-child")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"]")