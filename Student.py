class Student:
    name = ""
    grade = 0
    def __init__(self, name, grade) -> None:
        self.name = name
        self.grade = grade
    
    def result (self):
        if self.grade > 5:
            print("El alumno {} ha aprobado con una nota de {}".format(self.name, self.grade))
        else:
            print("El alumno {} ha suspendido con una nota de {}".format(self.name, self.grade))
            
alumno1 = Student("Cristian", 7)
alumno2 = Student("Alv", 3)

alumno1.result()
alumno2.result()