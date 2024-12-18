'''
#AIM: Area of circle accept radius from user
print("Program no:1")
radius=float(input("Enter the area of circle"))
area_of_circle=3.14*radius*2
print("area_of_circle",area_of_circle)
print("\n\n\n")


#AIM: Accept name from user and print hello username eg Hello Raj
print("Program no:2")
username=input("Enter your username")
print("Welcome and Hello", username)
print("\n\n\n")



#AIM: Calculate program. Accept two numbers and print the +,-,*,/,**,//
print("Program no:3")
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
ans=x+y
print("Addition", ans)
print("Addition", x+y)
print("Subtraction", x-y)
print("Multiplication", x*y)
print("Division",x/y)
print("Floor division",x//y)
print("Power",x**y)
print("Modulo Divison",x%y)
'''
#AIM: Salary slip
print("Program no:4")
employee_name=input("Please enter the employee name:")
basic_salary=float(input("Please enter the basiuc salary:"))
hra=float(input("Please enter the HRA:"))
allowance=float(input("please enter the allowance:"))
deduction=float(input("please enter the deduction:"))

net_salary=basic_salary+hra+allowance+deduction

print("\n"+ "="*40)
print(" " *10 + "salary slip")
print("="*40)
print(f"Employee Name: {employee_name}")
print("="*40)
print(f"Basic Salary: {basic_salary:,.2f}")
print(f"HRA: {hra:,.2f}")
print(f"Allowance: {allowance:,.2f}")
print(f"Deduction: {deduction:,.2f}")
print("="*40)
print(f"Net salary: {net_salary:,.2f}")
print("="*40)

                



                



                





