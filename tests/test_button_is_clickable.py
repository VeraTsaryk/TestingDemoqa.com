from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains

def test_button_is_clickable():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get('https://demoqa.com/buttons')
    button_dynamic_click = browser.find_element(By.CSS_SELECTOR,'div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(3)>button')
    button_dynamic_click.click()
    text_dynamic_click = browser.find_element(By.ID, 'dynamicClickMessage')
    assert text_dynamic_click.is_displayed()

def test_button_is_double_clickable():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get('https://demoqa.com/buttons')
    action = ActionChains(browser)
    button_double_click = browser.find_element(By.ID, 'doubleClickBtn')
    action.double_click(button_double_click).perform()
    text_about_double_click = browser.find_element(By.ID, 'doubleClickMessage')
    assert text_about_double_click.is_displayed()


def test_button_is_right_clickable():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    browser.get('https://demoqa.com/buttons')
    action = ActionChains(browser)
    button_right_click = browser.find_element(By.ID, 'rightClickBtn')
    action.context_click(button_right_click).perform()
    text_right_click = browser.find_element(By.ID, 'rightClickMessage')
    assert text_right_click.is_displayed()


def test_check_that_button_yes_is_clickable():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/radio-button')
    yes_button = browser.find_element(By.CSS_SELECTOR, 'label[for= "yesRadio"]')
    yes_button.click()
    answer = browser.find_element(By.CLASS_NAME, 'text-success')
    assert answer.is_displayed()

def test_check_that_button_impressive_is_clickable():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/radio-button')
    impressive_button = browser.find_element(By.CSS_SELECTOR, 'label[for= "impressiveRadio"]')
    impressive_button.click()
    answer = browser.find_element(By.CLASS_NAME, 'text-success')
    assert answer.is_displayed()
