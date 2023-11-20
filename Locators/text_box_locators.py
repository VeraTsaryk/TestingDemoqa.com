from selenium.webdriver.common.by import By


class TextBoxLocators:
    full_name = (By.ID, 'userName')
    email = (By.ID, 'userEmail')
    current_address = (By.ID, 'currentAddress')
    permanent_address = (By.ID, 'permanentAddress')
    button_submit = (By.ID, 'submit')
    outputName = (By.CSS_SELECTOR, '#output #name')
    outputEmail = (By.CSS_SELECTOR, '#output #email')
    outputCurrentAddress = (By.CSS_SELECTOR, '#output #currentAddress')
    outputPermanentAddress = (By.CSS_SELECTOR, '#output #permanentAddress')
