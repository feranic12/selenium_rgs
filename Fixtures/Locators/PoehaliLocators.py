from selenium.webdriver.common.by import By


class PoehaliLocators:
    Insured0_Dob_Input = (By.ID, "insuredPerson-0-dob")
    Trip_Type_Button = (By.ID, "content.insConditions.insVariant.tripType-single")
    Country_Input = (By.ID, "react-select-2-input")
    Euro_Button = (By.ID, "content.insConditions.currency-EUR")
    F50000_Button = (By.ID, "content.insConditions.insVariant.risks.medical.limit-50000")
    Trip_Start_Input = (By.ID, "content-contract-departures")
    Trip_End_Input = (By.ID, "content-contract-arrival")
    Protection_Needed_Button = (By.ID, "content.insConditions.insVariant.risks.sport.on-true")
    Buy_Premium_Button = (By.CSS_SELECTOR, "table.t-table-0-2-11 tr:last-child > td:last-child > button:nth-child(2)")
    No_Options_Button = Insured0_Next_Button = Insurer_Next_Button = (By.CSS_SELECTOR, "div.text-right > button")
    Insured0_Lastname_Input = (By.ID, "insuredPerson-0-lastName")
    Insured0_Firstname_Input = (By.ID, "insuredPerson-0-firstName")
    Insured0_Middlename_Input = (By.ID, "insuredPerson-0-middleName")
    Insured0_Lastname_Lat_Input = (By.ID, "insuredPerson-0-lastNameLat")
    Insured0_Firstname_Lat_Input = (By.ID, "insuredPerson-0-firstNameLat")
    Insured0_Male_Button = (By.ID, "content.insConditions.insVariant.insurers[0].sex-male")
    Insured0_Document = (By.ID, "insuredPerson-0-document")
    Insured0_Next_Button = (By.CSS_SELECTOR, "div.text-right > button")
    Insurer_Lastname_Input = (By.ID, "content-policyHolder-lastName")
    Insurer_Firstname_Input = (By.ID, "content-policyHolder-firstName")
    Insurer_Middlename_Input = (By.ID, "content-policyHolder-middleName")
    Insurer_Dob_Input = (By.ID, "content-policyHolder-dob")
    Insurer_Phone_Input = (By.ID, "content-policyHolder-phone")
    Insurer_Document_Seria_Input = (By.ID, "content-policyHolder-document-seria")
    Insurer_Document_Number_Input = (By.ID, "content-policyHolder-document-number")
    Insurer_Email_Input = (By.ID, "content-policyHolder-email")
    Insurer_Email2_Input = (By.ID, "content-policyHolder-email2")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"")


