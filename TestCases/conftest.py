import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import options
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    # file = "C:\\Users\\Change Me\\Downloads\\chromedriver-win64 (3)\\chromedriver-win64\\chromedriver.exe"
    # file = "./chromedriver.exe"
    # service = ChromeService(executable_path=file)
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Edge()
    driver.get('https://admin-demo.nopcommerce.com/login')
    driver.implicitly_wait(10)
    driver.maximize_window()

    request.cls.driver = driver
    yield driver

    driver.close()
    driver.quit()