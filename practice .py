inp_pass = input("enter password  :")
passw = "Hritik"

if inp_pass != passw:
    print("wrong password try 2")
    inp_pass = input("enter password 2  :")
    if inp_pass != passw:
        print("wrong password try 1")
        inp_pass = input("enter password 3  :")
        if inp_pass != passw:
            print("wrong password try 0")
        else:
            print("right password 3")
            print('''1. Who invented Java Programming?
                1. ) Guido van Rossum
                2. ) James Gosling
                3. ) Dennis Ritchie
                4. ) Bjarne Stroustrupnswer 2''')
            ans1 = int(input("enter ans :"))
            if ans1 == 2:
                print("right answer")
                print('''2. Which component is used to compile, debug and execute the java programs?
                        1. ) JRE
                        2. ) JIT
                        3. ) JDK
                        4. ) JVM''')
                ans2 = int(input("enter ans"))
                if ans2 == 2:
                    print("right ans congrats")
                else:
                    print("wrong ans try next year")
            else:
                print("wrong ans try next year")
    else:
        print("right password 2")
        print('''1. Who invented Java Programming?
   1. ) Guido van Rossum
   2. ) James Gosling
   3. ) Dennis Ritchie
   4. ) Bjarne Stroustrupnswer 2''')
        ans1 = int(input("enter ans :"))
        if ans1 == 2:
            print("right answer")
            print('''2. Which component is used to compile, debug and execute the java programs?
                    1. ) JRE
                    2. ) JIT
                    3. ) JDK
                    4. ) JVM''')
            ans2 = int(input("enter ans"))    
            if ans2 == 2:
                print("right ans congrats")
            else:
                print("wrong ans try next year")
        else:
            print("wrong ans try next year")
else:
    print("right password")
    print('''1. Who invented Java Programming?
   1. ) Guido van Rossum
   2. ) James Gosling
   3. ) Dennis Ritchie
   4. ) Bjarne Stroustrupnswer 2''')
    ans1 = int(input("enter ans :"))
    if ans1 == 2:
            print("right answer")
            print('''2. Which component is used to compile, debug and execute the java programs?
                    1. ) JRE
                    2. ) JIT
                    3. ) JDK
                    4. ) JVM''')
            ans2 = int(input("enter ans"))      
            if ans2 == 2:
                print("right ans congrats")
            else:
                print("wrong ans try next year")
    else:
        print("wrong ans try next year")