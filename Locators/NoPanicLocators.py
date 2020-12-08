from selenium.webdriver.common.by import By

class NoPanicLocators:
    dob = (By.CSS_SELECTOR, "input[data-name=\"content.policyHolder.dob\"]")
    male = (By.ID, "content.policyHolder.sex-male")
    button1 = (By.CSS_SELECTOR, "table tr:last-child>td:nth-child(2)>button")
    insurer_lastname = (By.NAME, "content.policyHolder.lastName")
    insurer_firstname = (By.NAME, "content.policyHolder.firstName")
    insurer_middlename = (By.NAME, "content.policyHolder.middleName")
    insurer_phone = (By.NAME, "content.policyHolder.phone")
    insurer_email = (By.NAME, "content.policyHolder.email")
    insurer_email2 = (By.NAME, "content.policyHolder.email2")
    insurer_seria = (By.NAME, "content.policyHolder.document.seria")
    insurer_number = (By.NAME, "content.policyHolder.document.number")
    continue_button = (By.CSS_SELECTOR, "div.text-right>button")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"")