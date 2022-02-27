# 04. Email Validator:
import re


class EmailValidator:
    __EMAIL_SPLIT_REGEX = '[@.]'
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return self.min_length <= len(name)

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        (name, mail, domain) = re.split(EmailValidator.__EMAIL_SPLIT_REGEX, email)

        return self.__is_name_valid(name) \
            and self.__is_mail_valid(mail) \
            and self.__is_domain_valid(domain)

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
print(EmailValidator.__dict__)


# Private methods
# Consider a real life example, a car engine, which is made up of many parts like spark plug,
# valves, piston, etc. No user use these parts directly, rather they just know how to use
# the parts which uses them. This is what private methods are used for.
# It is used to hide the inner functionality of any class from the outside world.
#
# Private methods are those methods that should neither be accessed outside
# the class nor by any base class. In Python, there is no existence of
# Private methods that cannot be accessed except inside a class.
# However, to define a private method prefix the member name with double underscore “__”.
