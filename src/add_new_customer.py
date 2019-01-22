import pytest

from Chromedriver import DriverFactory
from pages.home import HomeUsersPage


@pytest.fixture
def driver(request):
    driver = DriverFactory().create_chrome_driver()
    request.addfinalizer(driver.quit)
    return driver


def test_add_new_customer(driver):
    HomeUsersPage(driver).login('a678@gmail.com', '123')


