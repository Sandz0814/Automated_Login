import time
import pytest
from POM.LoginPage import LoginPages
from TestData.data import TestData


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login(self, setup):
        self.driver = setup
        self.login = LoginPages(self.driver)

        assert "Admin area demo" in self.login.verify_logo()

        userdata = TestData.multiple_login()

        for user in userdata:
            self.login.verify_input_email(user['email'])
            self.login.verify_input_password(user['password'])
            self.login.verify_login_btn()

            if user['expected'] == LoginPages.expected_invalid_email:
                assert LoginPages.expected_invalid_email in self.login.verify_invalid_email_message()
                print('Negative test with invalid Email and valid Password . Passed!')

            elif user['expected'] == LoginPages.expected_invalid_password:
                assert LoginPages.expected_invalid_password in self.login.verify_invalid_password_message()
                print('Negative test with valid Email and invalid Password . Passed!')

            elif user['expected'] == LoginPages.expected_invalid_email_format:
                assert LoginPages.expected_invalid_email_format in self.login.verify_invalid_email_format_message()
                print('Negative test with invalid Email format. Passed!')

            elif user['expected'] == LoginPages.expected_no_email_input:
                assert LoginPages.expected_no_email_input in self.login.verify_invalid_no_email_input()
                print('Negative test with no email. Passed!')

            elif user['expected'] == LoginPages.expected_success_login:
                assert LoginPages.expected_success_login in self.login.verify_success_login_message()
                print('Positive test with valid Email and valid Password . Passed!')



















