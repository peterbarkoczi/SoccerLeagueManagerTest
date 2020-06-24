from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self, driver=webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = "http://localhost:3001/"

    def navigate_to(self, page_url):
        self.driver.get(self.base_url + page_url)
