from collections import defaultdict

class School:
    def __init__(self):
        self.grades = defaultdict(list)
        self.students = []
        self.additions = []

    def add_student(self, name, grade):
        if name not in self.students:
            self.students.append(name)
            self.grades[grade].append(name)
            self.additions.append(True)
        else:
            self.additions.append(False)

    def roster(self):
        students_by_grade = []
        for grade_num in sorted(self.grades.keys()):
            students_by_grade += self.grade(grade_num)

        return students_by_grade

    def grade(self, grade_number):
        return sorted(self.grades[grade_number])

    def added(self):
        return self.additions
