from selenium.webdriver.common.by import By
from selenium import webdriver


def test_check_that_button_is_clickable():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/elements')
    radio_button = browser.find_element(By.CSS_SELECTOR, 'div[class ="element-list collapse show"] #item-2')
    radio_button.click()
    yes_button = browser.find_element(By.CSS_SELECTOR, 'label[for= "yesRadio"]')
    yes_button.click()
    answer = browser.find_element(By.CLASS_NAME, 'text-success')
    assert answer.is_displayed()
    impressive_button = browser.find_element(By.CSS_SELECTOR, 'label[for= "impressiveRadio"]')
    impressive_button.click()
    assert answer.is_displayed()
   # no_button = browser.find_element(By.CLASS_NAME, 'custom-control-label disabled')
    #no_button.click()
    #assert not no_button.click()


