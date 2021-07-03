# Расчет средней оценки за лекции или домашние задания лекторов/студентов
def average_rating(grades):
    summ = 0
    summ_1 = 0
    score_1 = 0
    for grade in grades.values():
        for score in grade:
            summ_1 = sum(grade)
            if len(grade) != 0:
                score_1 = summ_1/len(grade)
            else:
                print('Ошибка')
        summ += score_1
    if len(grades) != 0:
        return summ/len(grades)
    else:
        print('Ошибка')


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0

    # Оценки от студентов лекторам за лекции и средние оценки за лекции
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and \
                course in self.courses_in_progress and course in \
                lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                lecturer.average_rating = average_rating(lecturer.grades)
            else:
                lecturer.grades[course] = [grade]
                lecturer.average_rating = average_rating(lecturer.grades)
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'''\n{self.__class__.__name__}''' \
              f'''\nИмя: {self.name}\nФамилия: {self.surname}''' \
              f'''\nCредняя оценка за лекции: {self.average_rating}''' \
              f'''\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}''' \
              f'''\nЗавершенные курсы: {', '.join(self.finished_courses)}\n\n'''
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка. Экземпляр не относится к студентам!')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.average_rating = 0


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'\n{self.__class__.__name__}\n' \
              f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Cредняя оценка за лекции: {self.average_rating}\n\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка. Экземпляр не относится к лекторам!')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    # Оценки от преподавателей стундентам за домашние задания
    # и средние оценки за домашние задания
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course \
                in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.average_rating = average_rating(student.grades)
            else:
                student.grades[course] = [grade]
                student.average_rating = average_rating(student.grades)
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'\n{self.__class__.__name__}\n' \
              f'Имя: {self.name}\nФамилия: {self.surname}\n\n'
        return res
