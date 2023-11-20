from selenium.webdriver.common.by import By


class BookLocators:
    book = (By.ID, 'see-book-Git Pocket Guide')
    add_to_collection_button = (By.CSS_SELECTOR, 'div[class = "text-right fullButton"] #addNewRecordButton')
    user_profile = (By.CSS_SELECTOR, '.accordion :nth-child(6) > div > ul> li:nth-child(3)')
    login_form = (By.ID, 'login')
    search_field = (By.ID, 'searchBox')
    login_button_in_profile = (By.CSS_SELECTOR, '#notLoggin-label > a:nth-child(1)')
    button_go_to_store = (By.ID, 'gotoStore')
    delete_button = (By.ID, 'delete-record-undefined')
    small_modal = (By.ID, 'closeSmallModal-ok')
    book_store = (By.CLASS_NAME, 'main-header')
