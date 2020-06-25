from test.test_base import BaseTest
from Pages.sub_league_page import SubLeaguePage
from Pages.cups_page import CupsPage
from Pages.teams_page import TeamsPage


class LeaguePageTest(BaseTest):

    def test_league_name_is_appeared(self):
        expected = "Újbuda Liga"
        self.main_page.go_to_league_page()
        result = self.league_page.get_league_name()
        self.assertEqual(expected, result)

    def test_sub_league_page_is_appeared(self):
        sub_league_page = SubLeaguePage(self.driver)
        expected = "Bajnokság"
        self.main_page.go_to_league_page()
        self.league_page.click_on_sub_league_button()
        result = sub_league_page.get_title()
        self.assertEqual(expected, result)

    def test_cups_page_is_appeared(self):
        cups_page = CupsPage(self.driver)
        expected = "Kupák"
        self.main_page.go_to_league_page()
        self.league_page.click_on_cups_button()
        result = cups_page.get_title()
        self.assertEqual(expected, result)

    def test_teams_page_is_appeared(self):
        teams_page = TeamsPage(self.driver)
        expected = "Csapatok"
        self.main_page.go_to_league_page()
        self.league_page.click_on_teams_button()
        result = teams_page.get_title()
        self.assertEqual(expected, result)
