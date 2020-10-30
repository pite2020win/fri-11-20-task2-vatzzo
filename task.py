class Student:
    def __init__(self, name, surname, grade):
        self.name = name
        self.surname = name
        self.grade = grade
        self.marks = []
        self.avg = 0
        self.attendance = 0
        self.attendancePer = 0

    def addGrade(self, mark):
        self.marks.append(mark)

    def calcAverage(self):
        sum = 0
        for i in range(len(self.marks)):
            sum = sum + self.marks[i]

        self.avg = sum / len(self.marks)

    def checkAttendance(self, bool1):
        if bool1 == true:
            self.attendance += 1

    def checkTotalAttendance(self, NoOfClasses):
        self.attendancePer = self.attendance / NoOfClasses


st1 = Student('Mateusz', 'Kata', 1)
st1.addGrade(5)
st1.addGrade(6)
print(st1.name)
print(st1.marks)
st1.calcAverage()
print(st1.avg)
