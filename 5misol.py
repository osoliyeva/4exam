class Employee:
    def __init__(self,surname,position,salary) :
        self.surname=surname
        self.position=position
        self.salary=salary

class Enterprise_eployee(Employee):
    def __init__(self, surname, position, salary=int(),rating=int()):
        super().__init__(surname, position, salary)
        self.rating=rating
    
    def improve(self):
        if self.rating>=60 and self.rating<75:
            self.salary=self.salary*1.2
        elif self.rating>=75 and self.rating<90:
            self.salary=self.salary*1.4
        elif self.rating>=90 and self.rating<=100:
            self.salary=self.salary*1.6
        print(f"{self.surname} ishchining reytingi {self.rating} oyligi {self.salary}")


surname=[]
position=[]
salary=[]
rating=[]

print("5 ta ishchi ma'lumotlarini kiritishingiz kerak")
for i in range(5):
    surname.append(input("ismi: "))
    position.append(input("lavozimi: "))
    salary.append(int(input("oyligi: ")))
    rating.append(int(input("reytingi: ")))

employe1=Enterprise_eployee(surname[0],position[0],salary[0],rating[0])
employe2=Enterprise_eployee(surname[1],position[1],salary[1],rating[1])
employe3=Enterprise_eployee(surname[2],position[2],salary[2],rating[2])
employe4=Enterprise_eployee(surname[3],position[3],salary[3],rating[3])
employe5=Enterprise_eployee(surname[4],position[4],salary[4],rating[4])

print(employe1.improve())
print(employe2.improve())
print(employe3.improve())
print(employe4.improve())
print(employe5.improve())
