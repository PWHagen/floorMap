__author__ = 'Patrick Hagen'


class Employee:
    def __init__(self):
        self.name = ""
        self.cube = ""
        self.department = ""
        self.phone_number = ''

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_cube(self, cube):
        self.cube = cube

    def get_cube(self):
        return self.cube

    def set_department(self, department):
        self.department = department

    def get_department(self):
        return self.department

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number



