from pytest_bdd import scenarios, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from constants.constant import Constant
from pageobjectmodel.login import Login
from selenium.webdriver.support import expected_conditions as EC

scenarios("C:/Users/harikrishna.manokara/PycharmProjects/sauce_demo/tests/features/login.feature")


@when("I login with the standard_user credentials")
def login_standard_user(driver):
    '''This method is used to login the saucedemo page with standard user credentials'''
    # username
    user_name = driver.find_element_by_xpath(Login.user_name_loc)
    user_name.send_keys(Constant.STANDARD_USER)
    # password
    password = driver.find_element_by_xpath(Login.password_loc)
    password.send_keys(Constant.PASSWORD)
    # login
    login_button = driver.find_element_by_xpath(Login.login_button_loc)
    login_button.click()


@when('I login with the user credentials "<username>" and "<Password>"')
def login_standarduser(driver, username, Password):
    driver.maximize_window()
    # userName
    user_name = driver.find_element_by_xpath(Login.user_name_loc)
    user_name.send_keys(username, str)
    # password
    password = driver.find_element_by_xpath(Login.password_loc)
    password.send_keys(Password, str)
    # login
    login_button = driver.find_element_by_xpath(Login.login_button_loc)
    login_button.click()

@then("I validate the home page")
def validate_home_page(driver):
    "This method is used to validate the home page with the help of logo and URl verification"
    driver.find_element_by_xpath(Login.logo_loc).is_displayed()
    assert driver.current_url == Constant.HOME_PAGE_URL