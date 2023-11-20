from selenium.webdriver.common.by import By


class AgeLocators:
    edit_field_age = (By.CSS_SELECTOR, '.rt-tbody > div:nth-child(1) .rt-td:nth-child(3)')
    rename_button = (By.ID, 'edit-record-1')
    field_age = (By.ID, 'age')
    submit_button = (By.ID, 'submit')

