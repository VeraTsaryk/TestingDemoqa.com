from selenium.webdriver.common.by import By
from PageObject.base_page import BasePage
from selenium.webdriver import ActionChains


class ClickPage(BasePage):
    double_click_button = (By.ID, 'doubleClickBtn')
    button_right_click = (By.ID, 'rightClickBtn')
    button_dynamic_click = (By.CSS_SELECTOR, 'div.col-12.mt-4.col-md-6 > div:nth-child(2) > div:nth-child(3)>button')
    yes_button = (By.CSS_SELECTOR, 'label[for= "yesRadio"]')
    impressive_button = (By.CSS_SELECTOR, 'label[for= "impressiveRadio"]')
    text_dynamic_click = (By.ID, 'dynamicClickMessage')
    text_about_double_click = (By.ID, 'doubleClickMessage')
    text_right_click = (By.ID, 'rightClickMessage')
    answer = (By.CLASS_NAME, 'text-success')

    def __init__(self, driver):
        super().__init__(driver)

    def double_click(self):
        action = ActionChains(self.driver)
        double_click_address = self.find(self.double_click_button)
        action.double_click(double_click_address).perform()


    def right_click_button(self):
        action = ActionChains(self.driver)
        right_click_address = self.find(self.button_right_click)
        action.double_click(right_click_address).perform()

    def open_page(self, url):
        return self.driver.get(url)
