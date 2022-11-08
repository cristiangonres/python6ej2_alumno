class Student:
    name = ""
    grade = 0
    def __init__(self, name, grade) -> None:
        self.name = name
        self.grade = grade
    
    def result (self, name, grade):
        if grade > 5:
            print("El alumno {} ha aprobado con una nota de {}".format(name, grade))
        else:
            print("El alumno {} ha suspendido con una nota de {}".format(name, grade))
            
cristian = Student("Cristian", 7)
alv = Student("Alv", 3)
print(cristian.name)
print(cristian.grade)
cristian.result(cristian.name, cristian.grade)
alv.result(alv.name, alv.grade)