import unittest
from Tests.base_test import BaseTest


class MainPageTest(BaseTest):

    def test_main_page_is_appeared(self):
        self.main_page.go_to_main_page()
        app_title = "Soccer League Manager"
        self.assertEquals(app_title, self.main_page.get_app_title())

    def test_leagues_list_is_appeared(self):
        self.main_page.go_to_main_page()
        expected_list = ["Liga:", 2]
        result_list = [self.main_page.get_league_list_title(), self.main_page.get_league_list()]
        self.assertListEqual(expected_list, result_list)

    def test_login_buttons_are_appeared(self):
        self.main_page.go_to_main_page()
        expected = ["Bejelentkezés", "Regisztráció"]
        result = self.main_page.get_login_buttons()
        self.assertListEqual(expected, result)

    def test_click_on_first_league(self):
        self.main_page.go_to_main_page()
        self.main_page.click_on_league()
        self.assertTrue(self.league_page.menu_is_appeared())


if __name__ == "__main__":
    unittest.main()
