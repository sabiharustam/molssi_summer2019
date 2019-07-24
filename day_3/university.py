class Student:
	def __init__(self, name, surname, age, gender):
		self.name = name
		self.surname = surname
		self.age = age
		self.gender = gender
		self.courses = []

	def enroll(self, coursename):
		# write an enrollment method that takes in a course and adds it to the student courses.
		"""This function takes students name and addes courses when they select a course.

		Arguments
		_________
		name : str 
			name of the students. so the function know where to add the courses to.
		courses: str
			name of courses or id of courses to be added to the list.
		Returns
		_______
		
		"""
		if isinstance(coursename, list):
			self.courses.extend(coursename)
		else:
			self.courses.append(coursename)

	def __str__(self):
		return 'name' + self.surname + ',' + self.name + '\ncourses: ' + str(self.courses)

student1 = Student("Sam", "Ellis", 30, "Male")
stusent1.enroll("Math 101")
student1.enroll(["Phys 101", "Chem 101"]) 
print(student1.courses)

class Faculty:                             
    def __init__(self, name, surname, age, gender, position):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.courses = []
		self.position = position

    def assign_course(self, coursename):
        # write an enrollment method that takes in a course and adds it to the student courses.
        """This function takes students name and addes courses when they select a course.

        Arguments
        _________
        name : str 
            name of the students. so the function know where to add the courses to.
        courses: str
            name of courses or id of courses to be added to the list.
        Returns
        _______
        
        """
        if isinstance(coursename, list):
            self.courses.extend(coursename)
        else:
            self.courses.append(coursename)

    def __str__(self):
        return 'name' + self.surname + ',' + self.name + '\ncourses: ' + str(self.courses)