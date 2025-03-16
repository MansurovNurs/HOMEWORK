class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f'FULL NAME: {self.full_name} AGE: {self.age} IS_MARRIED: {self.is_married}')

class Student(Person):
    def __init__(self, full_name, age, is_married, marks=None):
        super().__init__(full_name, age, is_married)
        self.marks = marks
        self.marks = {}

    def average_mark(self):
            return sum(self.marks.values()) / len(self.marks) if self.marks else 0
    def add_mark(self, subject, mark):
        self.marks[subject] = mark

class Teacher(Person):
    base_salary = 300
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience > 3:
            per_year = self.experience - 3
            return self.base_salary + self.base_salary * 0.05 * per_year
        else:
            return self.base_salary
teacher1 = Teacher('Nursultan', 29, 'married',5)
print(f'TEACHERS NAME: {teacher1.full_name} AGE: {teacher1.age} MARRITAL STATUS: {teacher1.is_married} SALARY: {teacher1.calculate_salary()}')
def create_students():
    student1 = Student('Beka', 24, 'unmarried')
    student2 = Student('Dauren', 18, 'married')
    student3 = Student('Alina', 21, 'unmarried')
    return [student1, student2, student3]
print('STUDENTS INFO:')
students = create_students()
students[0].add_mark('math', 54)
students[0].add_mark('biology', 78)
students[0].add_mark('physics', 90)
students[1].add_mark('math', 32)
students[1].add_mark('biology', 45)
students[1].add_mark('physics', 65)
students[2].add_mark('math', 98)
students[2].add_mark('biology', 87)
students[2].add_mark('physics', 95)

for student in students:
    print(f'NAME: {student.full_name} AGE: {student.age} IS_MARRIED: {student.is_married}')
    print(f'MARK:{student.marks}')
    print(f'AVERAGE MARK: {round(student.average_mark(), 1)}')