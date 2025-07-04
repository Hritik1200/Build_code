# Grade checker


name = input("enter name : ")
print("name = ",name)

roll_no = int(input("enter roll no  : "))
print("roll no = ",roll_no)

java = int(input("enter java marks : "))
if java<20:
    print(java,"java fail")
elif java >100:
    print("invalid input")
else:
    print(java,"java pass")

c = int(input("enter c marks : "))
if c<20:
    print(c,"c fail")
elif c >100:
    print("invalid input")
else:
    print(c,"c pass")

python = int(input("enter python marks : "))
if python<20:
    print(python,"PYTHON fail")
elif python >100:
    print("invalid input")
else:
    print(python,"PYTHON pass")

go = int(input("enter go marks : "))
if go<20:
    print(go,"GO fail")
elif go >100:
    print("invalid input")
else:
    print(go,"GO pass")

ML = int(input("enter ML marks : "))
if ML<20:
    print(ML,"ML fail")
elif ML >100:
    print("invalid input")
else:
    print(ML,"ML pass")

DSA = int(input("enter DSA marks : "))
if DSA<20:
    print(DSA,"DSA fail")
elif DSA >100:
    print("invalid input")
else:
    print(DSA,"DSA pass")


# checking result pass or fail
if java<20 or c<20 or python<20 or go <20 or ML<20 or DSA<20:
    print("result : Fail")
elif java>100 or c>100 or python>100 or go >100 or ML>100 or DSA>100:
    print("invalid input")
else:
    print("result : Pass")

# checking total
total = (java+c+python+go+ML+DSA)
if total <=600:
    print("Total = ",total)
else:
    print("invalid input")

# checking percentage
per = round((java+c+python+go+ML+DSA)/600*100,2)
if per<=100:
    print("per = ",per,"%")
else:
    print("invalid input")

# checking grade
if per >=95 and per<=100:
    print("grade A+")
elif per >=85 and per <95:
    print("grade A")
elif per >=60 and per <85:
    print("grade B")
elif per >=35 and per <60:
    print("grade C")
elif per >100:
    print("invalid input")
else:
    print("fail")

