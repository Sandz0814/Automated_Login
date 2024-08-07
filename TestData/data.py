class TestData:
    @staticmethod
    def multiple_login():
        users = [
            {
                "email": "admin@yourstor.com",
                "password": "admin",
                "expected": "No customer account found"
            },
            {
                "email": "admin@yourstore.com",
                "password": "administrator",
                "expected": "The credentials provided are incorrect"
            },
            {
                "email": "adminyourstore.com",
                "password": "admin",
                "expected": "Please enter a valid email address."
            },
            {
                "email": "",
                "password": "admin",
                "expected": "Please enter your email"
            },
            {
                "email": "admin@yourstore.com",
                "password": "admin",
                "expected": "Logout"
            }
        ]

        return users





