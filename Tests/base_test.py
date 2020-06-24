import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.main_page import MainPage
from Pages.league_page import LeaguePage


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.main_page = MainPage(self.driver)
        self.league_page = LeaguePage(self.driver)

    def tearDown(self):
        self.driver.quit()
