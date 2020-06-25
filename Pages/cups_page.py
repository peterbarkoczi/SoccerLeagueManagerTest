from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class CupsPage(BasePage):

    title = (By.ID, 'cupsTitle')

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.title)).text
