import pytest

from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    global driver
    service_obj = Service("C:/Users/hp/Desktop/browerDriver/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)

    driver.get("https://www.facebook.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()