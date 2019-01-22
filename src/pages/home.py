from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomeUsersPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login(self, login, password):
        self.driver.get('http://users.bugred.ru/')
        self.driver.find_elements_by_css_selector(".newlink")[1].click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.col-md-6')))
        self.driver.find_element_by_css_selector("input[name='login']").clear()
        self.driver.find_element_by_css_selector("input[name='login']").send_keys(login)
        self.driver.find_elements_by_css_selector("input[name='password']")[0].clear()
        self.driver.find_elements_by_css_selector("input[name='password']")[0].send_keys(password)




