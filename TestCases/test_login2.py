import time
import pytest
from POM.LoginPage import LoginPages
from TestData.data import TestData


@pytest.mark.usefixtures("setup")
class TestLogin:

    expected_success_login = 'Logout'
    expected_invalid_password = 'The credentials provided are incorrect'
    expected_invalid_email = 'No customer account found'
    expected_invalid_email_format = 'Please enter a valid email address.'
    expected_no_email_input = 'Please enter your email'

    def test_login(self, setup):
        self.driver = setup
        self.login = LoginPages(self.driver)

        assert "Admin area demo" in self.login.verify_logo()

        userdata = TestData.multiple_login()

        for user in userdata:
            self.login.verify_input_email(user['email'])
            self.login.verify_input_password(user['password'])
            self.login.verify_login_btn()














