from selenium.webdriver.common.by import By


class LoginLocators:
    email_address_field = (By.ID, "userName")
    password_field = (By.ID, "password")
    login_button = (By.ID, 'login')
    warning_message = (By.CLASS_NAME, 'mb-1')
    log_out_button = (By.CSS_SELECTOR, 'div[class = "text-right col-md-5 col-sm-12"] #submit')
    login_name = (By.ID, 'userName-value')
    user_form = (By.CSS_SELECTOR, '#userForm > div:nth-child(1)')
    actual_name = (By.ID, 'userName-value')