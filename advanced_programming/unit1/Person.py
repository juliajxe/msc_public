class Name():
    def __init__(self, title, firstName, surname, otherNames=[]):
        self.title = title
        self.firstName = firstName
        self.otherNames = otherNames
        self.surname = surname

    def initials(self):
        names = [self.firstName] + self.otherNames
        inits = [name[0].upper() + "." for name in names]
        return " ".join(inits)

    def formalName(self):
        return f"{self.title} {self.initials()} {self.surname}"


class Person(object):
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def personalDetails(self):
        return self.name.formalName(), self.address, self.age


class Tutor(Person):
    id = 0

    def __init__(self, name, address, age, salary, id):
        super(Tutor, self).__init__(name, address, age)
        self.salary = salary
        self.id = id

    def personalDetails(self):
        return super(Tutor, self).personalDetails(), \
               self.salary, self.id


class Student(Person):
    def __init__(self, name, address, age, id):
        super(Student, self).__init__(name, address, age)
        self.id = id

    def personalDetails(self):
        return super(Student, self).personalDetails(), self.id


class DistanceStudent(Student):
    def __init__(self, name, address=None, age=None, id=None,
                 currentModule=None):
        super(DistanceStudent, self).__init__(name, address, age, id)
        self.currentModule = currentModule

    def isStudying(self):
        name = self.name.formalName()

        if self.currentModule is None:
            module = "nothing"
        else:
            module = f"the {self.currentModule} module"

        return f"{name} is studying {module}"
