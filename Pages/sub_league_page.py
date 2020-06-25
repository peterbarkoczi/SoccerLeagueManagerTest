from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class SubLeaguePage(BasePage):

    title = (By.ID, 'subLeagueTitle')
    sub_league_link = (By.CLASS_NAME, 'subLeague')
    league_detail_title = (By.ID, 'leagueDetailTitle')
    league_detail_table = (By.ID, 'leagueDetailTable')
    team_link = (By.CLASS_NAME, 'team')

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.title)).text

    def get_sub_leagues_list(self):
        return self.wait.until(EC.visibility_of_all_elements_located(self.sub_league_link))

    def click_on_sub_league(self, sub_league_name):
        self.driver.find_element_by_link_text(sub_league_name).click()

    def get_league_detail_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.league_detail_title)).text

    def get_league_detail_table(self):
        return self.wait.until(EC.visibility_of_element_located(self.league_detail_table)).is_displayed()

    def get_teams_links(self):
        return self.wait.until(EC.visibility_of_all_elements_located(self.team_link))

    def get_team_name_from_link(self):
        team_links = self.get_teams_links()
        return team_links[0].text

    def click_on_team_link(self, team):
        self.driver.find_element_by_link_text(team).click()

    def get_current_url(self):
        return self.driver.current_url
