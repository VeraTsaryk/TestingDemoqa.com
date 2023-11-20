from selenium.webdriver.common.by import By


class DialogsLocators:
    small_model = (By.ID, 'showSmallModal')
    large_model = (By.ID, 'showLargeModal')
    modal_title = (By.CLASS_NAME, 'modal-title')

