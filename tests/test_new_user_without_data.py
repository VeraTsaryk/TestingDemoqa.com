from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_new_user_error():
    #test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
    #options: Options = Options()
    #options.add_argument("--headless")
    #options.add_argument("--window-size=1920,1080")
    #options.add_argument(f'--user-agent={test_ua}')
    #options.add_argument('--no-sandbox')
    #options.add_argument("--disable-extensions")
    browser = webdriver.Chrome()
    solver = RecaptchaSolver(driver=browser)
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/login')
    new_user_button = browser.find_element(By.ID, 'newUser')
    new_user_button.click()
    first_name = browser.find_element(By.ID, 'firstname')
    first_name.send_keys('Fill')
    last_name = browser.find_element(By.ID, 'lastname')
    last_name.send_keys('Jons')
    user_name = browser.find_element(By.ID, 'userName')
    user_name.send_keys('Filly')
    password = browser.find_element(By.ID, 'password')
    password.send_keys('123456')
    recaptcha_iframe = browser.find_element(By.ID, 'recaptcha-anchor')
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)
    register_button = browser.find_element(By.ID, 'register')
    register_button.click()
    password_error = browser.find_element(By.CLASS_NAME, 'mb-1')
    error_text = 'Passwords must have at least one non alphanumeric character, one digit ("0"-"9"), one uppercase ("A"-"Z"), one lowercase ("a"-"z"), one special character and Password must be eight characters or longer.'
    assert password_error.text == error_text
