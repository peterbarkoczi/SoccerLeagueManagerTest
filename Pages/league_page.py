from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class LeaguePage(BasePage):

    menu = (By.CLASS_NAME, 'menu')
    league_name = (By.ID, 'leagueName')
    sub_league_button = (By.ID, 'navButtonSubLeague')
    cups_button = (By.ID, 'navButtonCups')
    teams_button = (By.ID, 'navButtonTeams')

    def __init__(self, driver):
        super().__init__(driver)

    def menu_is_appeared(self):
        return self.wait.until(EC.visibility_of_element_located(self.menu))

    def get_league_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.league_name)).text

    def click_on_sub_league_button(self):
        self.wait.until(EC.element_to_be_clickable(self.sub_league_button)).click()

    def click_on_cups_button(self):
        self.wait.until(EC.element_to_be_clickable(self.cups_button)).click()

    def click_on_teams_button(self):
        self.wait.until(EC.element_to_be_clickable(self.teams_button)).click()
