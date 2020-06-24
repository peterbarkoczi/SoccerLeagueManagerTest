from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class LeaguePage(BasePage):

    menu = (By.CLASS_NAME, 'menu')

    def __init__(self, driver):
        super().__init__(driver)

    def menu_is_appeared(self):
        return self.wait.until(EC.visibility_of_element_located(self.menu))