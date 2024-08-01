import pytest
from POM.LoginPage import LoginPages


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login(self, setup):
        self.driver = setup
        self.login = LoginPages(self.driver)

        assert "Admin area demo" in self.login.verify_logo()

        self.login.verify_input_email('admin@yourstore.com')

        self.login.verify_input_password('admin')

        self.login.verify_login_btn()

        assert 'Logout' in self.login.verify_login_if_successful()























