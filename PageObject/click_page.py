from PageObject.base_page import BasePage
from selenium.webdriver import ActionChains
from Locators.click_locators import ClickLocators


class ClickPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def double_click(self):
        action = ActionChains(self.driver)
        double_click_address = self.find(*ClickLocators.double_click_button)
        action.double_click(double_click_address).perform()

    def right_click_button(self):
        action = ActionChains(self.driver)
        right_click_address = self.find(*ClickLocators.button_right_click)
        action.context_click(right_click_address).perform()

    def actual_message_is_displayed(self):
        return self.is_displayed(ClickLocators.actual_message)

    def actual_text_about_double_click_is_displayed(self):
        return self.is_displayed(ClickLocators.text_about_double_click)

    def actual_text_about_right_click_is_displayed(self):
        return self.is_displayed(ClickLocators.text_right_click)

    def answer_is_displayed(self):
        return self.is_displayed(ClickLocators.answer)


