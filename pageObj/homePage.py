from selenium.webdriver.common.by import By


class HomePage:
    check_profile_name = (By.XPATH, "(//span[normalize-space()='Aditya Singh'])[1]")
    click_inner = (By.XPATH, "//a[@href='/settings']")
    click_setting = (By.XPATH, "//span[text()='Settings & privacy']")
    click_account = (By.XPATH, "(//*[name()='svg'][@aria-label='Your profile'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def check_user_name(self):
        return self.driver.find_element(*HomePage.check_profile_name)

    def clickAccount(self):
        return self.driver.find_element(*HomePage.click_account).click()

    def clickSetting(self):
        return self.driver.find_element(*HomePage.click_setting).click()

    def click_inner_setting(self):
        return self.driver.find_element(*HomePage.click_inner).click()
