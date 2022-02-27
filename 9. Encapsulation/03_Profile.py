# 03. Profile:

class Profile:
    def __init__(self, username: str, password: str):
        self.__username = self.validate_username(username)
        self.__password = self.validate_password(password)

    def validate_username(self, username):
        if 5 <= len(username) <= 15:
            return username
        raise ValueError("The username must be between 5 and 15 characters.")


    def validate_password(self, password):
        num_char = len(password)
        num_upper = len([i for i in password if i.isupper()])
        num_digits = len([i for i in password if i.isdigit()])

        if num_char < 8 or 0 >=  num_upper or 0 >= num_digits :
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        return password

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# print(profile_with_invalid_password)
profile_with_invalid_username = Profile('Too_long_username', 'Any')
print(profile_with_invalid_username)
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)
