# grade checker


name = input("enter name : ")
print("name = ",name)

roll_no = int(input("enter roll no  : "))
print("roll no = ",roll_no)

java = int(input("enter java marks : "))
if java<20:
    print(java,"java fail")
else:
    print(java,"java pass")

c = int(input("enter c marks : "))
if c<20:
    print(c,"c fail")
else:
    print(c,"c pass")

python = int(input("enter python marks : "))
if python<20:
    print(python,"PYTHON fail")
else:
    print(python,"PYTHON pass")

go = int(input("enter go marks : "))
if go<20:
    print(go,"GO fail")
else:
    print(go,"GO pass")

ML = int(input("enter ML marks : "))
if ML<20:
    print(ML,"ML fail")
else:
    print(ML,"ML pass")

DSA = int(input("enter DSA marks : "))
if DSA<20:
    print(DSA,"DSA fail")
else:
    print(DSA,"DSA pass")

if java<20 or c<20 or python<20 or go <20 or ML<20 or DSA<20:
    print("result : Fail")
else:
    print("result : Pass")


total = (java+c+python+go+ML+DSA)
print("Total = ",total)
per = round((java+c+python+go+ML+DSA)/600*100,2)
print("per = ",per,"%")

if per >=95 and per<=100:
    print("grade A+")
elif per >=85 and per <95:
    print("grade A")
elif per >=60 and per <85:
    print("grade B")
elif per >=35 and per <60:
    print("grade C")
else:
    print("fail")
