from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Pages.base_page import BasePage


class TeamsPage(BasePage):

    title = (By.ID, 'teamsTitle')
    add_team_button = (By.ID, 'addTeamButton')
    team_list = (By.ID, 'teamsList')
    add_new_team_modal = (By.ID, 'addNewTeam')
    modal_add_name = (By.ID, 'addName')
    modal_add_league = (By.ID, 'addLeague')
    modal_submit_button = (By.ID, 'addTeamSubmit')
    team = (By.XPATH, '//*[@id="teamsList"]/div')

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.title)).text

    def click_on_add_team_button(self):
        self.wait.until(EC.element_to_be_clickable(self.add_team_button)).click()

    def add_new_team_modal_is_appeared(self):
        return self.wait.until(EC.visibility_of_element_located(self.add_new_team_modal)).is_displayed()

    def fill_name_input_field(self, name):
        input_field = self.wait.until(EC.visibility_of_element_located(self.modal_add_name))
        input_field.send_keys(name)

    def select_from_sub_leagues(self, sub_league):
        select = Select(self.driver.find_element(*self.modal_add_league))
        select.select_by_visible_text(sub_league)

    def click_on_submit(self):
        self.wait.until(EC.element_to_be_clickable(self.modal_submit_button)).click()

    def get_team(self, team_name):
        teams = self.wait.until(EC.visibility_of_all_elements_located(self.team))
        for team in teams:
            if team.text == team_name:
                return True
        return False
