import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    # Initialize Chrome options
    # options = Options()
    # options.add_argument("--headless")
    # driver = webdriver.Edge(options=options)
    driver = webdriver.Chrome()
    driver.get('https://admin-demo.nopcommerce.com/login')
    driver.implicitly_wait(10)
    driver.maximize_window()

    request.cls.driver = driver
    yield driver

    driver.close()
    driver.quit()