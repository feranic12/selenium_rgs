from selenium.webdriver.common.by import By


class MiteLocators:
    dob1 = (By.CSS_SELECTOR, "input[data-name=\"content.insuredPerson.list[0].dob\"]")
    button2 = (By.XPATH, "//table//tr[11]/td[2]/button[2]")
    #button1 = (By.CSS_SELECTOR, r"table tr:last-child>td:nth-child(2)>button:first-child")
    lastname = (By.NAME, "content.insuredPerson.list[0].lastName")
    firstname = (By.NAME, "content.insuredPerson.list[0].firstName")
    middlename = (By.NAME, "content.insuredPerson.list[0].middleName")
    male = (By.ID, "content.insuredPerson.list[0].sex-male")
    is_insured = (By.CSS_SELECTOR, "label[for=\"insuredPerson-0-isInsured\"]")
    Continue_Button1 = (By.CSS_SELECTOR, "div.text-right>button")
    phone = (By.NAME, "content.policyHolder.phone")
    email = (By.NAME, "content.policyHolder.email")
    email2 = (By.NAME, "content.policyHolder.email2")
    seria = (By.NAME, "content.policyHolder.document.seria")
    number = (By.NAME, "content.policyHolder.document.number")
    Continue_Button2 = (By.CSS_SELECTOR, "div.text-right>button")
    Accept_All_Input = (By.CSS_SELECTOR, "label[for=\"content.temp.acceptAll_custom_input\"")


