class Book:
    def __init__(self,name,price=int(),page_count=int()) :
        self.name=name
        self.page_count=page_count
        self.price=price
    
    def add_page(self):
        self.page_count+=10
        if self.page_count>100:
            self.price*=2
        print(f"{self.name} kitobni sahifalar soni {self.page_count} va narxi {self.price}")


nom=[]
price=[]
count=[]

print("5 ta kitob nomi sahifalari soni va narxini kiritishingiz kerak.")
for i in range(5):
    nom.append(input("kitob nomini kiriting: "))
    price.append(int(input("kitob narhini kiriting: ")))
    count.append(int(input("kitob sahifalari sonini kiriting: ")))

book1=Book(nom[0],price[0],count[0])
book2=Book(nom[1],price[1],count[1])
book3=Book(nom[2],price[2],count[2])
book4=Book(nom[3],price[3],count[3])
book5=Book(nom[4],price[4],count[4])

print(book1.add_page())
print(book2.add_page())
print(book3.add_page())
print(book4.add_page())
print(book5.add_page())