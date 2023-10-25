from selenium.webdriver.common.by import By
from selenium import webdriver


def test_model_dialogs_are_displayed():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/modal-dialogs')
    browser.find_element(By.ID, 'showSmallModal').click()
    modal_body = browser.find_element(By.CLASS_NAME, 'modal-title')
    assert modal_body.is_displayed()
    assert modal_body.text == 'Small Modal'
    browser.find_element(By.ID, 'closeSmallModal').click()
    browser.find_element(By.ID, 'showLargeModal').click()
    modal_title = browser.find_element(By.CLASS_NAME, 'modal-title')
    assert modal_title.is_displayed()
    assert modal_title.text == 'Large Modal'
