import time

from selenium.webdriver.common.by import By


class PrivacySetting:
    # set locator path
    get_email_id = (
    By.XPATH, "//li[@data-testid='settings_section_email']//strong[contains(text(),'adityyasingh6010@gmail.com')]")
    frame_switch = (By.TAG_NAME, "iframe")
    click_block_list = (By.XPATH, "//span[text()='See your blocked list']")
    total_block = (By.XPATH, "(//div[@class='bdao358l om3e55n1 g4tp4svg alzwoclg cqf1kptm jez8cy9q gvxzyvdx'])[3]//span[@class = 'gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas m2nijcs8 szxhu1pg hpj0pwwo sggt6rq5 tpi2lg9u pbevjfx6 ztn2w49o']")
    click_profile = (By.XPATH, "(//*[name()='svg'][@aria-label='Your profile'])[1]")
    click_logout = (By.XPATH, "(//span[normalize-space()='Log Out'])[1]")
    click_privacy = (By.XPATH, "//span[normalize-space()='Privacy']")
    click_manage_profile = (By.XPATH, "(//div[normalize-space()='Manage your profile'])")
    get_mobile = (By.XPATH, "//span[normalize-space()='086208 12140']")
    click_blocking = (By.XPATH, "(//span[normalize-space()='Blocking'])[1]")
    click_to_user_block = (By.XPATH, "(//div[@aria-label='Edit'])[2]")
    click_close_symbol = (By.XPATH, "(//div[@aria-label='Close'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def get_email_id_meth(self):
        self.driver.switch_to.frame(self.driver.find_elements(*PrivacySetting.frame_switch)[0])
        resp = self.driver.find_element(*PrivacySetting.get_email_id).text
        return resp

    # switch to the default frame
    def click_privacy_meth(self):
        self.driver.switch_to.default_content()
        """click privacy"""
        return self.driver.find_element(*PrivacySetting.click_privacy).click()

    def click_manage_profile_meth(self):
        time.sleep(2)
        self.driver.switch_to.frame(self.driver.find_elements(*PrivacySetting.frame_switch)[0])
        return self.driver.find_element(*PrivacySetting.click_manage_profile).click()

    def get_mobile_number(self):
        return self.driver.find_element(*PrivacySetting.get_mobile)

    def back(self):
        return self.driver.back()

    def click_to_blocking_meth(self):
        return self.driver.find_element(*PrivacySetting.click_blocking).click()

    def click_to_user_block_meth(self):
        return self.driver.find_element(*PrivacySetting.click_to_user_block).click()

    def block_list_meth(self):
        return self.driver.find_element(*PrivacySetting.click_block_list).click()

    def count_blocks(self):
        count = self.driver.find_elements(*PrivacySetting.total_block)
        return count

    def click_close_symbol_meth(self):
        return self.driver.find_element(*PrivacySetting.click_close_symbol).click()

    def click_profile_meth(self):
        return self.driver.find_element(*PrivacySetting.click_profile).click()

    def click_logout_meth(self):
        return self.driver.find_element(*PrivacySetting.click_logout).click()
