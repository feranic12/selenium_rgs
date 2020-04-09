from selenium.webdriver.common.by import By


class MiteLocators:
    dob1 = (By.ID, "insuredPerson-0-dob")
    button2 = (By.XPATH, "//table//tr[11]/td[2]/button[2]")
    #button1 = (By.CSS_SELECTOR, r"table tr:last-child>td:nth-child(2)>button:first-child")
    lastname = (By.ID, "content-insuredPerson-list-0--lastName")
    firstname = (By.ID, "content-insuredPerson-list-0--firstName")
    middlename = (By.ID, "content-insuredPerson-list-0--middleName")
    male = (By.ID, "content.insuredPerson.list[0].sex-male")
    is_insured = (By.ID, "content-insuredPerson-list-0--isPolicyHolder")
    phone = (By.ID, "content-policyHolder-phone")
    email = (By.ID, "content-policyHolder-email")
    email2 = (By.ID, "content-policyHolder-email2")
    seria = (By.ID, "content-policyHolder-document-seria")
    number = (By.ID, "content-policyHolder-document-number")
    continue_button = (By.CSS_SELECTOR, "div.text-right>button")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"")


