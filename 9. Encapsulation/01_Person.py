# 01. Person:

class Person:

    def __init__(self, name, age):
        # double underscore in python - Private Attribute
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())

# Double underscore prefix
# In Python, we use double underscore i.e., __ before the attribute's name and
# those attributes will not be directly accessible/visible outside.
# Double underscore mangles the attribute's name. However, that variable
# can still be accessed using some tricky syntax but it's generally
# not a good idea to do so. Double underscores are used for fully private variables.
#
# According to Python documentation −#
# If your class is intended to be subclassed, and you have attributes that
# you do not want subclasses to use, consider naming them with double leading
# underscores and no trailing underscores. This invokes Python's name mangling
# algorithm, where the name of the class is mangled into the attribute name.
# This helps avoid attribute name collisions should subclasses
# inadvertently contain attributes with the same name.
