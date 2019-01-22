import os
from os.path import join as join_paths
from selenium import webdriver


class DriverFactory:
    def __init__(self):
        self.home_dir = os.getenv('HOME')

    def create_chrome_driver(self):
            driver_location = join_paths(self.home_dir, 'bin', 'chromedriver')
            return webdriver.Chrome(driver_location)


