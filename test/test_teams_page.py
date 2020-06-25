from test.test_base import BaseTest
from Pages.teams_page import TeamsPage
from ddt import ddt, file_data


@ddt
class TeamsPageTest(BaseTest):

    def go_to_teams_page(self):
        self.main_page.go_to_league_page()
        self.league_page.click_on_teams_button()

    def test_add_team_modal_is_appeared(self):
        teams_page = TeamsPage(self.driver)
        self.go_to_teams_page()
        teams_page.click_on_add_team_button()
        self.assertTrue(teams_page.add_new_team_modal_is_appeared())

    @file_data('resources/add_new_team_resources.json')
    def test_add_new_team(self, team, sub_league):
        teams_page = TeamsPage(self.driver)
        self.go_to_teams_page()
        teams_page.click_on_add_team_button()
        teams_page.fill_name_input_field(team)
        teams_page.select_from_sub_leagues(sub_league)
        teams_page.click_on_submit()
        self.assertTrue(teams_page.get_team(team))
