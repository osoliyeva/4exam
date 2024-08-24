sekund=open("3misol.txt","w")
soniya=int(input("sekundlarni kiriting: "))
kun=soniya//86400
soat=(soniya-kun*86400)//3600
minut=(soniya-kun*86400-soat*3600)//60
sekunt=soniya-kun*86400-soat*3600-minut*60

sekund.write(f"kiritilgan sekundlar: {soniya}\n")
sekund.write(f"kun: {kun}, soat: {soat}, minut: {minut}, sekund:{sekunt}")
sekund.close()

sekund=open("3misol.txt","r")
print(sekund.read())