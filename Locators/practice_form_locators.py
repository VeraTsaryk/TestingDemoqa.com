from selenium.webdriver.common.by import By


class PracticeFormLocators:
    first_name_field = (By.ID, 'firstName')
    last_name_field = (By.ID, 'lastName')
    email_name_field = (By.CSS_SELECTOR, 'div [class = "col-md-9 col-sm-12"] #userEmail')
    gender = (By.CSS_SELECTOR, 'div [class = "col-md-9 col-sm-12"] #gender-radio-2')
    mobile_number_field = (By.CSS_SELECTOR, 'div[class ="col-md-9 col-sm-12"] #userNumber')
    date_of_birth = (By.ID, 'dateOfBirthInput')
    date_of_birth2 = (By.CSS_SELECTOR, 'div [aria-label = "Choose Tuesday, November 14th, 2023"]')
    hobbies = (By.ID, 'hobbies-checkbox-1')
    submit_button = (By.ID, 'submit')
    submitting_form = (By.CSS_SELECTOR, '.modal-content')