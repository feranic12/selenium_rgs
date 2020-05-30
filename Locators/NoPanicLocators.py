from selenium.webdriver.common.by import By

class NoPanicLocators:
    dob = (By.ID, "content-policyHolder-dob")
    male = (By.ID, "content.policyHolder.sex-male")
    button1 = (By.CSS_SELECTOR, "table tr:last-child>td:nth-child(2)>button")
    insurer_lastname = (By.ID, "content-policyHolder-lastName")
    insurer_firstname = (By.ID, "content-policyHolder-firstName")
    insurer_middlename = (By.ID, "content-policyHolder-middleName")
    insurer_phone = (By.ID, "content-policyHolder-phone")
    insurer_email = (By.ID, "content-policyHolder-email")
    insurer_email2 = (By.ID, "content-policyHolder-email2")
    insurer_seria = (By.ID, "content-policyHolder-document-seria")
    insurer_number = (By.ID, "content-policyHolder-document-number")
    continue_button = (By.CSS_SELECTOR, "div.text-right>button")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"")