from selenium.webdriver.common.by import By
from selenium import webdriver


def test_check_search_books():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get('https://demoqa.com/books')
    search_field = browser.find_element(By.ID, 'searchBox')
    book_name = 'Git Pocket Guide'
    search_field.send_keys(book_name)
    book = browser.find_element(By.ID, 'see-book-Git Pocket Guide')
    assert book.text == book_name
