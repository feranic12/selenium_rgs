from selenium.webdriver.common.by import By


class RodnyeStenyLocators:
    Area_Input = (By.NAME, "content.object.data.area")
    Region_Button = (By.ID,"content.object.data.flatbaseRegion-1")
    Owned_Button = (By.ID, "content.object.data.privat-yes")
    Rent_Button = (By.ID, "content.object.data.rent-yes")
    Fire_Button = (By.ID, "content.object.data.fire-yes")
    Constr_Svg = (By.CLASS_NAME, "css-19bqh2r")
    Constr_Hidden = (By.NAME, "content.object.data.construct.ss")
    Buy_Premium_Button = (By.CSS_SELECTOR, "div.card-group > div:nth-child(3) button")
    Begin_Date_Input = (By.CSS_SELECTOR, "div.input-group > input")
    Region_Input = (By.ID, "react-select-5-input")
    City_Input = (By.NAME, "content.object.data.address.registration.city.name")
    Street_Input = (By.NAME, "content.object.data.address.registration.street.name")
    House_Input = (By.NAME, "content.object.data.address.registration.house")
    Corp_Input = (By.NAME, "content.object.data.address.registration.corp")
    Building_Input = (By.NAME, "content.object.data.address.registration.building")
    Flat_Input = (By.NAME, "content.object.data.address.registration.flat")
    Calc_Next_Button = (By.CSS_SELECTOR, "div.text-right > button")
    InsurersLastName_Input = (By.NAME, "content.policyHolder.lastName")
    InsurersFirstName_Input = (By.NAME, "content.policyHolder.firstName")
    InsurersMiddleName_Input = (By.NAME, "content.policyHolder.middleName")
    InsurersDob_Input = (By.CSS_SELECTOR, "input[data-name=\"content.policyHolder.dob\"]")
    InsurersPhone_Input = (By.NAME, "content.policyHolder.phone")
    InsMale_Button = (By.ID, "content.policyHolder.sex-male")
    InsEmail_Input = (By.NAME, "content.policyHolder.email")
    InsEmail2_Input = (By.NAME, "content.policyHolder.email2")
    InsDocumentSeria_Input = (By.NAME, "content.policyHolder.document.seria")
    InsDocumentNumber_Input = (By.NAME, "content.policyHolder.document.number")
    Insurer_Next_Button = (By.CSS_SELECTOR, "div.text-right > button")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"")
