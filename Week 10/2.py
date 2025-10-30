#dictanary
Student_grades = {
    'gorge' : 95,
    'jerry' : 72,
    'amanda' : 84}
def calc():
    values = Student_grades.values()
    sumofnumbers = sum(values)
    avrage = sumofnumbers / len(Student_grades)
    print(f'the class avrage is {avrage}')
calc()