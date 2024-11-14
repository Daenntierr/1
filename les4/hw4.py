class Man(object):
    height = 175

class Student(Man):
    money = 200

class Worker(Man):
    money = 400

class ItStepStudent(Student):
    crystals = 1000

student1 = Student()
worker1 = Worker()
it_student = ItStepStudent()

print(student1.height)
print(student1.money)
print("+++")
print(worker1.height)
print(worker1.money)