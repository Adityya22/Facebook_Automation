from selenium.webdriver.common.by import By
from config.config_data import TestData


class LoginPage:

    User_name = (By.XPATH, "//input[@name='email']")
    Password = (By.XPATH, "//input[@name='pass']")
    Login_click = (By.XPATH, "//button[@name='login']")

    def __init__(self, driver):
        self.driver = driver

    def user_name(self):
        return self.driver.find_element(*LoginPage.User_name).send_keys(TestData.USER_NAME)

    def password(self):
        return self.driver.find_element(*LoginPage.Password).send_keys(TestData.PASSWORD)

    def login_button(self):
        return self.driver.find_element(*LoginPage.Login_click).click()
