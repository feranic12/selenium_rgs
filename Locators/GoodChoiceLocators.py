from selenium.webdriver.common.by import By


class GoodChoiceLocators:
    Button_Prolongation_False = (By.ID, "content.contract.data.prolongation.is-false")
    Continue_Button1 = (By.CSS_SELECTOR,"div.table-responsive>table button")
    Region_Input = (By.CSS_SELECTOR, "div.SelectFieldInner__value-container")
    City = (By.NAME, "content.object.data.address.registration.city.name")
    Street = (By.NAME, "content.object.data.address.registration.street.name")
    House = (By.NAME, "content.object.data.address.registration.house")
    Corp = (By.NAME, "content.object.data.address.registration.corp")
    Building = (By.NAME, "content.object.data.address.registration.building")
    Flat = (By.NAME, "content.object.data.address.registration.flat")
    Continue_Button2 = (By.CSS_SELECTOR, "div.text-right>button")
    Surname = (By.NAME, "content.policyHolder.lastName")
    First_Name = (By.NAME, "content.policyHolder.firstName")
    Middle_Name = (By.NAME, "content.policyHolder.middleName")
    Dob  = (By.CSS_SELECTOR, "input[data-name=\"content.policyHolder.dob\"]")
    Phone = (By.NAME, "content.policyHolder.phone")
    Male = (By.ID, "content.policyHolder.sex-male")
    EMail1 = (By.NAME, "content.policyHolder.email")
    EMail2 = (By.NAME, "content.policyHolder.email2")
    Passport_Seria = (By.NAME, "content.policyHolder.document.seria")
    Passport_Number = (By.NAME, "content.policyHolder.document.number")
    Passport_Date = (By.ID, "content-policyHolder-document-doi")
    Passport_Issued = (By.ID, "content-policyHolder-document-issued")
    Passport_Department = (By.ID, "content-policyHolder-document-departmentCode")
    Citizenship = (By.ID, "content-policyHolder-citizenship-name")
    SNILS = (By.ID, "content-policyHolder-snils")
    INN = (By.ID, "content-policyHolder-inn")
    Birth_Place = (By.ID, "content-policyHolder-birthPlace-name")
    Continue_Button3 = (By.CSS_SELECTOR, "div.text-right>button")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"]")



