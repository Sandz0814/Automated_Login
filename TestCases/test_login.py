import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class TestLogin:

    def test_login(self):

        driver = webdriver.Chrome()
        driver.get('https://admin-demo.nopcommerce.com/login')
        driver.implicitly_wait(10)
        driver.maximize_window()

        logo = driver.find_element(By.XPATH, "//h1[normalize-space()='Admin area demo']")
        logo_text = logo.text
        assert "Admin area demo" in logo_text

        email = driver.find_element(By.XPATH, "//input[@id='Email']")
        email.clear()

        email.send_keys('admin@yourstore.com')

        password = driver.find_element(By.XPATH, "//input[@id='Password']")
        password.clear()

        password.send_keys('admin')

        login_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
        login_btn.click()

        logout = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").is_displayed()

        if logout:
            print('User Successfully logging in')
            assert True










