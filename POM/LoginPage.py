from selenium.webdriver.common.by import By


class LoginPages:

    logo = "//h1[normalize-space()='Admin area demo']"
    email = "//input[@id='Email']"
    password = "//input[@id='Password']"
    login_btn = "//button[normalize-space()='Log in']"
    logout_text = "//a[normalize-space()='Logout']"

    success_login_message = "//a[normalize-space()='Logout']"
    invalid_email_message = "//li[normalize-space()='No customer account found']"
    invalid_password_message = "//li[normalize-space()='The credentials provided are incorrect']"
    invalid_email_format_message = "//span[@class='field-validation-error']"
    invalid_no_email_input = "//span[@id='Email-error']"

    expected_success_login = 'Logout'
    expected_invalid_password = 'The credentials provided are incorrect'
    expected_invalid_email = 'No customer account found'
    expected_invalid_email_format = 'Please enter a valid email address.'
    expected_no_email_input = 'Please enter your email'

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

    def verify_success_login_message(self):
        return self.driver.find_element(By.XPATH, self.success_login_message).text

    def verify_invalid_email_message(self):
        return self.driver.find_element(By.XPATH, self.invalid_email_message).text

    def verify_invalid_password_message(self):
        return self.driver.find_element(By.XPATH, self.invalid_password_message).text

    def verify_invalid_email_format_message(self):
        return self.driver.find_element(By.XPATH, self.invalid_email_format_message).text

    def verify_invalid_no_email_input(self):
        return self.driver.find_element(By.XPATH, self.invalid_no_email_input).text





