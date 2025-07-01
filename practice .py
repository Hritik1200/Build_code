   # Set your password :
   # p4n@in
   # Enter your Password : 
   # p4n
   # wrong password ... try 2 more time out of 2
   # p4n@
   # wrong password ... try 1 more time 1
   # p4n@34
   # wrong password ... try 0 more time 0
   # note : user select right password
   # then start MCQ EXAM...
   
    
   # 1. Who invented Java Programming?
   # 1. ) Guido van Rossum
   # 2. ) James Gosling
   # 3. ) Dennis Ritchie
   # 4. ) Bjarne Stroustrup
   
   # Select Answer 2
   
   # wrong answer [ Try Next year ] 
   
   # Note :if select Right Answer 
   # ask 2nd Question ...
   
   # 2. Which component is used to compile, debug and execute the java programs?
   # 1. ) JRE
   # 2. ) JIT
   # 3. ) JDK
   # 4. ) JVM
   
   # Select Answer 2 ... con..


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
                4. ) Bjarne Stroustrup''')
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
         4. ) Bjarne Stroustrup''')
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
      4. ) Bjarne Stroustrup''')
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
