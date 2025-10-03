class Student:
    name = "N/A"
    age = 0
    siblings = 0
    numPets = 0
    teacherName = "N/A"

    def __init__(self, name, age, siblings, numPets, teacher):
        self.name = name
        self.age = age

    def doDrama(self):
        print("Alas poor Yoric, I knew him Horatio")

    def doMaths(num1, num2):
        return num1 + num2

    def getOlder(years):
        years.age += 1
    
student1 = Student("Jack", 13, 0, 0, "Mr Smiley")

student2 = Student("Penny", 12, 2, 1 , "Ms Gumpton")

print(student1.name, "is", student1.age, "and has", student1.siblings, "sibling(s)")
print(student2.name, "is", student2.age, "and has", student2.siblings, "sibling(s)")

student1.name = "Jack"
print(student1.name)

student1.doDrama()

print(student2.doMaths(12, 7))

print(student1.age)
print(student2.age)
student1.getOlder(1)
print(student1.age)
print(student2.age)

student1.doMaths()
