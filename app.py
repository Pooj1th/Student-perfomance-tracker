from flask import Flask, render_template, request, redirect, url_for
import json
from student import Student

app = Flask(__name__)
DATA_FILE = 'students.json'

def load_students():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return [Student.from_dict(s) for s in data]
    except:
        return []

def save_students(students):
    with open(DATA_FILE, 'w') as f:
        json.dump([s.to_dict() for s in students], f)

@app.route('/')
def index():
    students = load_students()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll_number = request.form['roll_number']
        students = load_students()
        if any(s.roll_number == roll_number for s in students):
            return "Roll number already exists!"
        student = Student(name, roll_number)
        students.append(student)
        save_students(students)
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/add_grades', methods=['GET', 'POST'])
def add_grades():
    students = load_students()
    if request.method == 'POST':
        roll_number = request.form['roll_number']
        subject = request.form['subject']
        grade = float(request.form['grade'])
        for s in students:
            if s.roll_number == roll_number:
                s.add_grade(subject, grade)
                save_students(students)
                return redirect(url_for('index'))
        return "Student not found!"
    return render_template('add_grades.html', students=students)

@app.route('/view_student/<roll_number>')
def view_student(roll_number):
    students = load_students()
    for s in students:
        if s.roll_number == roll_number:
            return render_template('view_student.html', student=s)
    return "Student not found."

if __name__ == '__main__':
    app.run(debug=True)
