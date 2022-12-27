from selenium.webdriver.common.by import By


class GoodChoiceLocators:
    Button_Prolongation_False = (By.CSS_SELECTOR, "div[data-name=\"content.contract.data.prolongation.is\"] button:first-child")
    Button1 = (By.CSS_SELECTOR, "div.mt-3 tr:last-child>td:nth-child(2)>button")
    AddressNew1 = (By.NAME, "content.object.data.address.registration.city.full")
    AddressNew2 = (By.NAME, "content.object.data.address.registration.addressCdi.short")
    Flat = (By.NAME, "content.object.data.address.registration.flat")
    Continue_Button2 = (By.CSS_SELECTOR, "div.text-right>button")
    Surname = (By.NAME, "content.policyHolder.lastName")
    First_Name = (By.NAME, "content.policyHolder.firstName")
    Middle_Name = (By.NAME, "content.policyHolder.middleName")
    Dob  = (By.NAME, "content.policyHolder.dob")
    Phone = (By.NAME, "content.policyHolder.phone")
    Male = (By.CSS_SELECTOR, "div[data-name=\"content.policyHolder.sex\"] button:first-child")
    EMail1 = (By.NAME, "content.policyHolder.email")
    EMail2 = (By.NAME, "content.policyHolder.email2")
    Passport_Seria = (By.NAME, "content.policyHolder.document.seria")
    Passport_Number = (By.NAME, "content.policyHolder.document.number")
    Continue_Button3 = (By.CSS_SELECTOR, "div.text-right>button")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"]")



