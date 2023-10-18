from selenium.webdriver.common.by import By
from selenium import webdriver


def test_change_users_information():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/elements')
    radio_button = browser.find_element(By.CSS_SELECTOR, 'div[class ="element-list collapse show"] #item-3')
    radio_button.click()
    rename_button = browser.find_element(By.ID, 'edit-record-1')
    rename_button.click()
    field_age = browser.find_element(By.ID, 'age')
    field_age.clear()
    field_age.send_keys(59)
    submit_button = browser.find_element(By.ID, 'submit')
    submit_button.click()
    change_field_age =browser.find_element(By.CSS_SELECTOR, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(1) > div > div:nth-child(3)')
    assert change_field_age.text == '59' # How do correct assert?
