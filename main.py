def average_grade(human):
    if isinstance(human, Lecturers) or isinstance(human, Student):
        summa = 0
        num = 0
        for i in human.grades:
            summa += sum(human.grades[i])
            num += len(human.grades[i])
        try:
            return summa / num
        except ZeroDivisionError:
            return 0


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturers) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {average_grade(self)}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
               f'Завершенные курсы: {self.finished_courses}\n\n'


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

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n\n'


class Lecturers(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {average_grade(self)}\n\n'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

some_student = Student('Rita', 'Smitt', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

cool_reviewers = Reviewers('Some', 'Buddy')
cool_reviewers.courses_attached += ['Python']
cool_reviewers.courses_attached += ['Git']

some_reviewers = Reviewers('Sem', 'Green')
some_reviewers.courses_attached += ['Python']
some_reviewers.courses_attached += ['Git']

cool_lecturer = Lecturers('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

some_lecturer = Lecturers('Sem', 'Green')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

best_student.rate_lw(cool_lecturer, 'Python', 10)
best_student.rate_lw(cool_lecturer, 'Python', 8)
best_student.rate_lw(cool_lecturer, 'Python', 10)
best_student.rate_lw(cool_lecturer, 'Git', 10)
some_student.rate_lw(some_lecturer, 'Python', 10)
some_student.rate_lw(some_lecturer, 'Python', 7)
some_student.rate_lw(some_lecturer, 'Python', 8)
some_student.rate_lw(some_lecturer, 'Git', 9)
some_student.rate_lw(some_lecturer, 'Git', 7)

cool_reviewers.rate_hw(best_student, 'Python', 10)
cool_reviewers.rate_hw(best_student, 'Python', 8)
cool_reviewers.rate_hw(best_student, 'Python', 9)
cool_reviewers.rate_hw(best_student, 'Git', 9)
cool_reviewers.rate_hw(best_student, 'Git', 9)

some_reviewers.rate_hw(some_student, 'Python', 9)
some_reviewers.rate_hw(some_student, 'Python', 8)
some_reviewers.rate_hw(some_student, 'Python', 6)
some_reviewers.rate_hw(some_student, 'Git', 8)
some_reviewers.rate_hw(some_student, 'Git', 9)

print(cool_reviewers)
print(some_reviewers)
print(best_student)
print(some_student)
print(cool_lecturer)
print(some_lecturer)
