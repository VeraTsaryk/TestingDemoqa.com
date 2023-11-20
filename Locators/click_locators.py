from selenium.webdriver.common.by import By


class ClickLocators:
    double_click_button = (By.ID, 'doubleClickBtn')
    button_right_click = (By.ID, 'rightClickBtn')
    button_dynamic_click = (By.CSS_SELECTOR, 'div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(3)>button')
    yes_button = (By.CSS_SELECTOR, 'label[for= "yesRadio"]')
    impressive_button = (By.CSS_SELECTOR, 'label[for= "impressiveRadio"]')
    text_dynamic_click = (By.ID, 'dynamicClickMessage')
    text_about_double_click = (By.ID, 'doubleClickMessage')
    text_right_click = (By.ID, 'rightClickMessage')
    answer = (By.CLASS_NAME, 'text-success')
    actual_message = (By.ID, 'dynamicClickMessage')
