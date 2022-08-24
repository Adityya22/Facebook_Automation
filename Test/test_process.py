import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config.config_data import TestData
from pageObj.homePage import HomePage
from pageObj.privacy_setting import PrivacySetting
from utility.basePage import BasePage
from pageObj.loginPage import LoginPage


class Test_process(BasePage):

    def test_verify_LoginPage_title(self):
        self.driver.implicitly_wait(10)
        login_page_title = self.driver.title
        # to verify loginPage title
        assert login_page_title == TestData.LOGIN_PAGE_TITLE
        self.message_logging("title verified successfully")

    def test_login(self):
        login_page = LoginPage(self.driver)
        # to enter username and password
        login_page.user_name()
        login_page.password()
        login_page.login_button()
        self.message_logging("login successfully")

    def test_home(self):
        """
        Creating object of Homepage
        """
        home = HomePage(self.driver)

        # validate profile name
        name = home.check_user_name().text
        print(name)
        assert name == TestData.PROFILE_NAME
        self.message_logging("User name is validated")

        """click to Account"""
        home.clickAccount()

        """click to settings"""
        self.wait_clickable(home.click_setting)
        home.clickSetting()

        """click to inner setting"""
        self.wait_clickable(home.click_inner)
        home.click_inner_setting()

    def test_privacy(self):

        privacy = PrivacySetting(self.driver)
        # privacy = PrivacySetting()

        # validate email-id
        self.wait_enable(privacy.frame_switch)
        email = privacy.get_email_id_meth()
        self.message_logging(email + "this is user email-id")
        assert email == TestData.USER_NAME

        # click to privacy
        privacy.click_privacy_meth()

        # click to manage profile
        privacy.click_manage_profile_meth()

        # Fetch the mobile number
        time.sleep(5)
        # self.wait_enable(privacy.get_mobile)
        number = privacy.get_mobile_number().text
        self.message_logging("the mobile number is "+number)
        assert number == '086208 12140'

        # back to privacy
        privacy.back()

        # click to blocking
        privacy.click_to_blocking_meth()

        # click to block user
        privacy.click_to_user_block_meth()

        # click block list
        privacy.block_list_meth()

        # count all block
        total_count = privacy.count_blocks()
        c = len(total_count)
        self.message_logging("total number of blockers " + str(c))

        # click the close symbol
        privacy.click_close_symbol_meth()

        # click account profile
        privacy.click_profile_meth()

        # logout
        privacy.click_logout_meth()
        self.driver.close()
