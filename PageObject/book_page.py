from PageObject.login_page import LoginPage
from Locators.book_locators import BookLocators


class BookPage(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_book(self):
        self.click(BookLocators.book)

    def click_add_to_collection_button(self):
        self.click(BookLocators.add_to_collection_button)

    def click_login_form(self):
        self.click(BookLocators.login_form)

    def click_user_profile(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click(BookLocators.user_profile)

    def set_search_field(self, book_name):
        self.set(BookLocators.search_field, book_name)

    def click_login_button_in_profile(self):
        self.click(BookLocators.login_button_in_profile)

    def click_button_go_to_store(self):
        self.click(BookLocators.button_go_to_store)

    def click_delete_button(self):
        self.click(BookLocators.delete_button)

    def click_close_small_model(self):
        self.click(BookLocators.small_modal)

    def book_is_displayed(self):
        return self.is_displayed(BookLocators.book)

    def book_store_is_displayed(self):
        return self.is_displayed(BookLocators.book_store)
