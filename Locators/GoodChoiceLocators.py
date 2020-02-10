from selenium.webdriver.common.by import By


class GoodChoiceLocators:
    Button1 = (By.CSS_SELECTOR, r"div.mt-3 tr:last-child>td:nth-child(2)>button")
    Button_Flat = (By.ID, r"content.object.data.type-flat")
    Region_Input = (By.ID, r"react-select-2-input")
    City = (By.ID, r"content-object-data-address-registration-city-name")
    Street = (By.ID, r"content-object-data-address-registration-street-name")
    House = (By.ID, r"content-object-data-address-registration-house")
    Corp = (By.ID, r"content-object-data-address-registration-corp")
    Building = (By.ID, r"content-object-data-address-registration-building")
    Flat = (By.ID, r"content-object-data-address-registration-flat")
    Continue_Button1 = (By.CSS_SELECTOR, r"div.text-right>button")
    Surname = (By.ID, r"content-policyHolder-lastName")
    First_Name = (By.ID, r"content-policyHolder-firstName")
    Middle_Name = (By.ID, r"content-policyHolder-middleName")
    Dob  = (By.ID, r"content-policyHolder-dob")
    Phone = (By.ID, r"content-policyHolder-phone")
    Male = (By.ID, r"content.policyHolder.sex-male")
    EMail1 = (By.ID, r"content-policyHolder-email")
    EMail2 = (By.ID, r"content-policyHolder-email2")
    Passport_Seria = (By.ID, r"content-policyHolder-document-seria")
    Passport_Number = (By.ID, r"content-policyHolder-document-number")
    Passport_Date = (By.ID, r"content-policyHolder-document-doi")
    Passport_Issued = (By.ID, r"content-policyHolder-document-issued")
    Passport_Department = (By.ID, r"content-policyHolder-document-departmentCode")
    Citizenship = (By.ID, r"content-policyHolder-citizenship-name")
    SNILS = (By.ID, r"content-policyHolder-snils")
    INN = (By.ID, r"content-policyHolder-inn")
    Birth_Place = (By.ID, r"content-policyHolder-birthPlace-name")
    Continue_Button2 = (By.CSS_SELECTOR, r"div.text-right>button")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"]")



