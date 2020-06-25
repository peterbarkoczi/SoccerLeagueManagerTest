from test.test_base import BaseTest
from Pages.sub_league_page import SubLeaguePage
from ddt import ddt, data, unpack


@ddt
class SubLeaguePageTest(BaseTest):

    @unpack
    @data((0, "Hétfő"),
          (1, "Kedd"),
          (2, "Szerda"),
          (3, "Csütörtök"),
          (4, "Péntek"))
    def test_sub_leagues_are_appeared(self, index, expected):
        sub_league_page = SubLeaguePage(self.driver)
        self.main_page.go_to_league_page()
        self.league_page.click_on_sub_league_button()
        sub_leagues_list = sub_league_page.get_sub_leagues_list()
        self.assertEqual(expected, sub_leagues_list[index].text)

    @data("Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek")
    def test_sub_league_details_appeared(self, sub_league_name):
        expected = [sub_league_name, True]
        sub_league_page = SubLeaguePage(self.driver)
        self.main_page.go_to_league_page()
        self.league_page.click_on_sub_league_button()
        sub_league_page.click_on_sub_league(sub_league_name)
        result = [
            sub_league_page.get_league_detail_title(),
            sub_league_page.get_league_detail_table()
                          ]
        self.assertListEqual(expected, result)

    def test_teams_link_is_working(self):
        sub_league_page = SubLeaguePage(self.driver)
        self.main_page.go_to_league_page()
        self.league_page.click_on_sub_league_button()
        sub_league_page.click_on_sub_league("Kedd")
        team = sub_league_page.get_team_name_from_link()
        sub_league_page.click_on_team_link(team)
        self.assertTrue(team.replace(' ', '') in sub_league_page.get_current_url())
