from selenium.webdriver.common.by import By


class GoodChoiceLocators:
    Button1 = (By.CSS_SELECTOR, "div.mt-3 tr:last-child>td:nth-child(2)>button")
    Button_Flat = (By.ID, "content.object.data.type-flat")
    Region_Input = (By.ID,"react-select-2-input")
    City = (By.ID, "content-object-data-address-registration-city-name")
    Street = (By.ID, "content-object-data-address-registration-street-name")
    House = (By.ID,"content-object-data-address-registration-house")
    Corp = (By.ID, "content-object-data-address-registration-corp")
    Building = (By.ID, "content-object-data-address-registration-building")
    Flat = (By.ID, "content-object-data-address-registration-flat")
    Continue_Button1 = (By.CSS_SELECTOR, "div.text-right>button")
    Surname = (By.ID, "content-policyHolder-lastName")
    First_Name = (By.ID, "content-policyHolder-firstName")
    Middle_Name = (By.ID, "content-policyHolder-middleName")
    Dob  = (By.ID, "content-policyHolder-dob")
    Phone = (By.ID, "content-policyHolder-phone")
    Male = (By.ID, "content.policyHolder.sex-male")
    EMail1 = (By.ID, "content-policyHolder-email")
    EMail2 = (By.ID, "content-policyHolder-email2")
    Passport_Seria = (By.ID, "content-policyHolder-document-seria")
    Passport_Number = (By.ID, "content-policyHolder-document-number")
    Passport_Date = (By.ID, "content-policyHolder-document-doi")
    Passport_Issued = (By.ID, "content-policyHolder-document-issued")
    Passport_Department = (By.ID, "content-policyHolder-document-departmentCode")
    Citizenship = (By.ID, "content-policyHolder-citizenship-name")
    SNILS = (By.ID, "content-policyHolder-snils")
    INN = (By.ID, "content-policyHolder-inn")
    Birth_Place = (By.ID, "content-policyHolder-birthPlace-name")
    Continue_Button2 = (By.CSS_SELECTOR, "div.text-right>button")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"]")



