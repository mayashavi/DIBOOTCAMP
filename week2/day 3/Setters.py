# SETTERS
import re
import datetime

class Person:
    def __init__(self, first_name, last_name, birth_date):
        self._first_name = self.format_name(first_name)
        self._last_name = self.format_name(last_name)
        self.birth_date = birth_date
        self._full_name = f"{self._first_name} {self._last_name}"   # protected
        self._salary = 35000                                        # protected

    @staticmethod
    def format_name(name):
        name = name.strip().capitalize()
        name = re.sub(r'[^a-zA-Z]', '', name)
        return name

    @classmethod
    def from_age(cls, first_name, last_name, age):
        current_year = datetime.datetime.today().year
        birth_year = current_year - age
        birth_date = f'1-1-{birth_year}'
        return cls(first_name, last_name, birth_date)

    # -------- ENCAPSULATED PROPERTIES -------- #

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = self.format_name(value)

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = self.format_name(value)
