from selenium.webdriver.common.by import By


class LoginPages:

    logo = "//h1[normalize-space()='Admin area demo']"
    email = "//input[@id='Email']"
    password = "//input[@id='Password']"
    login_btn = "//button[normalize-space()='Log in']"
    logout_text = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def verify_logo(self):
        logo = self.driver.find_element(By.XPATH, self.logo).text
        return logo

    def verify_input_email(self, user_email):
        self.driver.find_element(By.XPATH, self.email).clear()
        self.driver.find_element(By.XPATH, self.email).send_keys(user_email)

    def verify_input_password(self, user_password):
        self.driver.find_element(By.XPATH, self.password).clear()
        self.driver.find_element(By.XPATH, self.password).send_keys(user_password)

    def verify_login_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn).click()

    def verify_login_if_successful(self):
        logout_text = self.driver.find_element(By.XPATH, self.logout_text).text
        return logout_text
