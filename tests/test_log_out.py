from selenium.webdriver.common.by import By
from selenium import webdriver


def test_log_out():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/profile')
    browser.find_element(By.CSS_SELECTOR, '#notLoggin-label > a:nth-child(1)').click()
    user_name = browser.find_element(By.ID, 'userName')
    login = "Ola"
    user_name.send_keys(login)
    password = browser.find_element(By.ID, 'password')
    passwordName = '12345@Ola'
    password.send_keys(passwordName)
    login_button = browser.find_element(By.ID, 'login')
    login_button.click()
    profile_name = browser.find_element(By.ID, 'userName-value')
    assert profile_name.is_displayed()
    assert profile_name.text == 'Ola'
    log_out_button = browser.find_element(By.CSS_SELECTOR, 'div[class = "text-right col-md-5 col-sm-12"] #submit')
    log_out_button.click()
    user_form = browser.find_element(By.CSS_SELECTOR, '#userForm > div:nth-child(1)')
    assert profile_name != True
    assert user_form.is_displayed()