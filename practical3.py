'''
#BMI
wt=float(input("Enter weight in kgs"))
ht=float(input("Enter height in meters"))
bmi=wt/(ht*ht)
print("BMI=", bmi)

if(bmi<18.5):
    print("Your are underweight")
elif(bmi>=18.5) and (bmi<=24.9):
    print("Your are normal")
elif(bmi>=25) and (bmi<=29.9):
    print("Your are overweight")
elif(bmi>=30):
    print("Your are obese")
else:
    print("BMI not in range")
'''


'''
#grade
marks=float(input("Enter the student's marks:"))

def calculate_grade(marks):
       if marks>90:
            return"o"
       elif 85<=marks<90:
            return"A+"
       elif 80<=marks<85:
            return"A"
       elif 70<=marks<80:
            return"B+"
       elif 60<=marks<70:
            return"B"
       elif 50<=marks<60:
            return"C"
       elif 40<=marks<50:
            return"D"
       else:
            return"F"
grade=calculate_grade(marks)
print(f"The student's grade is:{grade}")
'''

'''
#Salary slip
print("SALARY PROGRAM")
name=input("Enter name of employee:")
role=input("Enter your role.")
salary=0

print()

if role=="SE":
    salary=15000
elif role=="SSE":
    salary=20000
elif role=="TL":
    salary=40000
elif role=="BA":
    salary=50000
elif role=="SR":
    salary=100000
elif role=="VP":
    salary=1000000
elif role=="CEO":
    salary=10000000


print("SALARY DETAILS")
print("NAME OF EMPLOYEE:",name)
print("BASC SALARY:",salary)
DA=(25/1000)*salary
print("DEARNESS ALLOW:",DA)
HRA=(15/100)*salary
print("HOUSE RENT ALLOW:",HRA)
TA=(7.5/100)*salary
print("TRAVEL ALLOW:",TA)

print()

net_pay=salary+DA+HRA+TA
print("NET SALARY PAY:",net_pay)
PF=(12/100)*salary
print("PROVIDENT FUND:",PF)
Tax=(5/100)*salary
print("TAX:",Tax)

print()

gross_pay=net_pay-Tax
print("GROSS PAYMENT:",gross_pay)
'''

#Odd or Even
num=int(input("enter a number:"))
def check_odd_even(number):
    if number%2==0:
        return f"{number} is even."
    else:
        return f"{number} is odd."
result=check_odd_even(num)
print(result)
