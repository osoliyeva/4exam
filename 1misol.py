mevalar=["Olma","Anor","Kartoshka","Kadi","Xurmo","Sabzi","Rediska","Ko'kat"]
a=[]
k=[]

for i in range(len(mevalar)):
    for j in range(len(mevalar[i])):
        if mevalar[i][j]=="A" or mevalar[i][j]=="a":
            if mevalar[i] not in a:
                a.append(mevalar[i])

        if mevalar[i][j]=="K" or mevalar[i][j]=="k":
            if mevalar[i] not in k:
                k.append(mevalar[i])

print(f"k harfli faylda  {k}")
print(f"a harfli faylda {a}")