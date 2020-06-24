from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class MainPage(BasePage):

    page_title = (By.ID, 'appTitle')
    league_list_title = (By.ID, 'leagueTitle')
    leagues_list = (By.CLASS_NAME, 'league')
    login_buttons = (By.XPATH, "//div[@class='login']/Button")
    first_league = (By.XPATH, "//*[@id='leaguesList']/div[1]/a")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_main_page(self):
        self.driver.get(self.base_url)

    def get_app_title(self):
        self.wait.until(EC.visibility_of_element_located(self.page_title))
        return self.driver.find_element(*self.page_title).text

    def get_league_list_title(self):
        self.wait.until(EC.visibility_of_element_located(self.league_list_title))
        return self.driver.find_element(*self.league_list_title).text

    def get_league_list(self):
        leagues = self.driver.find_elements(*self.leagues_list)
        return len(leagues)

    def get_login_buttons(self):
        buttons = self.wait.until(EC.visibility_of_all_elements_located(self.login_buttons))
        login_buttons = []
        for button in buttons:
            login_buttons.append(button.text)
        return login_buttons

    def click_on_league(self):
        self.wait.until(EC.element_to_be_clickable(self.first_league)).click()
