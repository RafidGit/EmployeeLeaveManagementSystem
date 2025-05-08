class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Employee(Person):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.role = 'employee'

class Manager(Person):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.role = 'manager'
