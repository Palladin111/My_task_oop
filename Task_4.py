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
    # Определим список студентов (для расчета средней оценки по курсу)
    list_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = 0
        # Добавим в список студентов каждый созданный экземпляр
        Student.list_students.append(self)

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
        res = f'''\n{self.__class__.__name__}'''\
                f'''\nИмя: {self.name}\nФамилия: {self.surname}'''\
                f'''\nCредняя оценка за лекции: {self.average_rating}'''\
                f'''\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}'''\
                f'''\nЗавершенные курсы: {', '.join(self.finished_courses)}\n'''
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
    # Определим список лекторов (для расчета средней оценки по курсу)
    list_lecturer = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        # Добавим в список лекторов каждый созданный экземпляр
        Lecturer.list_lecturer.append(self)

    def __str__(self):
        res = f'\n{self.__class__.__name__}\n' \
              f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Cредняя оценка за лекции: {self.average_rating}\n'
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
              f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


# Функция подсчета средней оценки  по всем студентам в рамках конкретного курса
def average_course_st(course):
    sum_score = 0
    average_score_list = []

    for stud in Student.list_students:
        for course_1 in stud.grades.items():
            if course.lower() == course_1[0].lower():
                sum_score = sum(course_1[1])/len(course_1[1])
                average_score_list.append(sum_score)

    if average_score_list != []:
        print(f'\nСредняя оценка за домашние задания  у всех студентов по '
              f'курсу {course} равна {sum(average_score_list)/len(average_score_list)}')
    else:
        print('\nОшибка. По данному курсу отстуствуют оценки или данный курс отсутствует.')


# Функция подсчета средней оценки  по всем лекторам в рамках конкретного курса
def average_course_lect(course):
    sum_score = 0
    average_score_list = []

    for lect in Lecturer.list_lecturer:
        for course_1 in lect.grades.items():
            if course.lower() == course_1[0].lower():
                sum_score = sum(course_1[1])/len(course_1[1])
                average_score_list.append(sum_score)

    if average_score_list != []:
        print(f'\nСредняя оценка за лекции  у всех лекторов по '
              f'курсу {course} равна {sum(average_score_list)/len(average_score_list)}')
    else:
        print('\nОшибка. По данному курсу отстуствуют оценки или данный курс отсутствует.')


student_1 = Student('Nic', 'Forn', 'male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Karl', 'Pig', 'male')
student_2.courses_in_progress += ['Java']
student_2.courses_in_progress += ['Python']
Reviewer_1 = Reviewer('Mark', 'Shagal')
Reviewer_1.courses_attached += ['Python']
Reviewer_1.rate_hw(student_1, 'Python', 8)
Reviewer_1.rate_hw(student_2, 'Python', 9)
Reviewer_2 = Reviewer('Gleb', 'Parhomenko')
Reviewer_2.courses_attached += ['Python']
Reviewer_2.courses_attached += ['Java']
Reviewer_2.rate_hw(student_1, 'Python', 4)
Reviewer_2.rate_hw(student_2, 'Java', 7)

lecturer_1 = Lecturer('Peter', 'Corobov')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Ivan', 'Kolobkov')
lecturer_2.courses_attached += ['Python']
student_1.rate_hw(lecturer_1,'Python', 5)
student_2.rate_hw(lecturer_1,'Python', 6)
student_1.rate_hw(lecturer_2,'Python', 9)
student_2.rate_hw(lecturer_2,'Python', 8)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(Reviewer_1)
print(Reviewer_2)

print(student_1 > student_2)
print(lecturer_2 > lecturer_1)

average_course_st('Python')
average_course_lect('Python')

