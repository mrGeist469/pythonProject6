class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewers(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturers(Mentor):
    def __init__(self, name):
        super().__init__(self, name)
        self.grades = {}



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_reviewers = Reviewers('Some', 'Buddy')
cool_reviewers.courses_attached += ['Python']

cool_reviewers.rate_hw(best_student, 'Python', 10)
cool_reviewers.rate_hw(best_student, 'Python', 10)
cool_reviewers.rate_hw(best_student, 'Python', 10)

print(best_student.grades)