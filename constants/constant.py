import os


class Constant:
    os.chdir("..")
    USER_HOME = "C:" + os.path.sep + "Users" + os.path.sep + "harikrishna.manokara" + os.path.sep + "PycharmProjects" + os.path.sep + "sauce_demo" + os.path.sep
    DRIVER_PATH = USER_HOME + 'driver' + os.path.sep + 'chromedriver.exe'
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"
    STANDARD_USER = "standard_user"
    PASSWORD = "secret_sauce"
