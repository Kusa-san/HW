class school:
#
    #class property
    number_of_instances = 0
    Class_1 = 0
    Class_2 = 0
    Class_3 = 0
    Class_4 = 0
#
    #properties
#
    def __init__(self,name,Class,grades):
        self.name=name
        self.Class=Class
        self.grades=grades
        school.number_of_instances += 1
        if self.Class == 1:
            school.Class_1 += 1
        elif self.Class == 2:
            school.Class_2 += 1
        elif self.Class == 3:
            school.Class_3 += 1
        elif self.Class == 4:
            school.Class_4 += 1
#
    #methods
#
    def info(self):
        print(f"Student Name is {self.name} and in Class {self.Class} with grade {self.grade}")
#
    @classmethod
    def student_per_class(cls,Class):
        if Class == 1:
            return cls.Class_1
        elif Class == 2:
            return cls.Class_2
        elif Class == 3:
            return cls.Class_3
        elif Class == 4:
            return cls.Class_4
#
#
    def GPA(self):
        gpa = 0
        for i in range (len(self.grades)):
            gpa +=self.grades[i]
        
            return gpa/len(self.grades)
#
    def introduction(self):
        print(f"Hi this is {self.name},I'm at the {self.Class} Class, and i scored {self.grades}")
#
    def __str__(self):
        return f"{self.name} is in the  {self.Class}-th Class"
#
kusa = school('Kusa', 4,[55,90,41])
ali = school('Ali Hassan', 4,[68,74,55])
kusa.introduction()
ali.introduction()
print(school.student_per_class(1))
print(ali)
print(kusa)
print(ali.GPA())