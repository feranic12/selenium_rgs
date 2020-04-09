from selenium.webdriver.common.by import By


class CascoProLocators:
    ButtonBuy1 = (By.CSS_SELECTOR, "table tr:last-child>td:nth-child(2)>button")
    Mk = (By.ID, "react-select-2-input")
    Model = (By.ID, "react-select-3-input")
    Year_Of_Issue = (By.CSS_SELECTOR, "div#wizard-container div.form-row:nth-child(2) div.SelectFieldClosed")
    VIN = (By.ID, "content-object-data-vin")
    Number = (By.ID, "content-object-data-gosNumber")
    Pts_Seria = (By.ID, "content-object-data-tsPassport-seria")
    Pts_Number = (By.ID, "content-object-data-tsPassport-number")
    Sts_Seria = (By.ID, "content-object-data-tsCard-seria")
    Sts_Number = (By.ID, "content-object-data-tsCard-number")
    Continue_Button = (By.CSS_SELECTOR, "div.text-right>button")
    LastName = (By.ID, "content-policyHolder-lastName")
    FirstName = (By.ID,"content-policyHolder-firstName")
    MiddleName = (By.ID, "content-policyHolder-middleName")
    Dob = (By.ID, "content-policyHolder-dob")
    Phone = (By.ID, "content-policyHolder-phone")
    Male = (By.ID, "content.policyHolder.sex-male")
    Email = (By.ID, "content-policyHolder-email")
    Email2 = (By.ID, "content-policyHolder-email2")
    Passport_Seria = (By.ID, "content-policyHolder-document-seria")
    Passport_Number = (By.ID, "content-policyHolder-document-number")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"")

