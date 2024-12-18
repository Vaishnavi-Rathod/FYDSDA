'''********************(WHILE LOOP)*********************'''

'''
#MENU CHOICE PROGRAM

print("MENU BASED PROGRAM")
while(True):
    print("select the Menu")
    print("1.Area of Triangle")
    print("2.Area of circle")
    print("3.Area of square")
    print("4.Exit")

    choice=int(input("Enter choice="))
    print("CHOICE=",choice)

    if choice==1:
         b=float(input("Enter a value for base:"))
         ht=float(input("Enter a value for height:"))
         area=1/2*(b*ht)
         print("Area of Triangle:",area)

    elif choice==2:
       r=float(input("Enter a value for radius:"))
       area=3.14*r*r
       print("Area of circle:")

    elif choice==3:
        s=float(input("Enter a value for side:"))
        area=s*s
        print("Area of square:".area)

    elif choice==4:
        print("Bye")
        break

    else:
        print("Enter a valid value:")
    break
'''
'''
#MULTIPICATION TABLE USING (WHILE LOOP)
number=int(input("Enter a number:"))
i=1
while i<=10:
    print(f"{number}x {i}={number *i}")
    i+=1
'''

'''
#CHOICE PROGRAM (using IF ELSE)
while(True):
    print("Welcome")
    print()
    print()
    choice=2
    if(choice==1):
        print("choice is 1")
        break
    elif(choice ==2):
        print("choice is 2")
        break
    elif(choice==3):
        print("choice is 3")
        break
    elif(choice==4):
        print("choice is 4")
        break
    else:
        print("choice Invalid")
        exit()

print("After while")
print("bye bye program ends")
'''
'''
#N number in series
i=1
while i<=100:
    print(i, end=" ")
    i+=1
'''

'''
#WAPP to print pattern
print("-----------")
print("Printing Pattern")
i=1
while(i<=3):
    print("#####")
    i=i+1
'''
#WAPP to check username or password is correct or not (using IF ELSE).
username=VaishnaviRathod
password=VAISHHNAVI
USERNAME=input("Enter your username")
PASSWORD=input("Enter your password")
if("USERNAME:",username) and ("PASSWORD:"):
   print("USERNAME and PASSWORD is correct")

             





         
         
  
  
