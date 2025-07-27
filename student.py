class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def to_dict(self):
        return {
            'name': self.name,
            'roll_number': self.roll_number,
            'grades': self.grades
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data['name'], data['roll_number'])
        student.grades = data.get('grades', {})
        return student
