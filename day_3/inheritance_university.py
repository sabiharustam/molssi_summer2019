class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.id = self.generate_id()
        self.courses = []

    def generate_id(self):
        id_hash = 0
        for s in self.name:
            id_hash += ord(s)
        for s in self.surname:
            id_hash += ord(s)
        id_hash = id_hash % 1000000000
        return id_hash

    def __str__(self):
        return 'name' + self.surname + ',' + self.name + '\ncourses: ' + str(self.courses)


class Student(Person):
    def __init__(self, name, surname, age, gender):
        super().__init__(name, surname, age, gender)


class Faculty(Person):
    def __init__(self, name, surname, age, gender, position):
        super().__init__(name, surname, age, gender)
        self.position = position


student1 = Student("Sam", "Ellis", 30, "Male")
# student1.enroll("Math 101")
# student1.enroll(["Phys 101", "Chem 101"])
print(student1.__dict__)

faculty1 = Faculty("Sabiha", "Rustam", 25, "Female", "Lecturer")
print(faculty1.__dict__)

