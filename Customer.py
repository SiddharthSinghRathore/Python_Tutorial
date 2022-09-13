from datetime import date

First_Name = input("Enter First Name:")
Last_Name = input("Enter Last Name:")
print("Date Of Birth")
DOB = int(input())
Employee = input("Enter Employee Id:")
Working_Company = input("Enter Working Company:")
Birth_Place = input("Enter Birth Palace:")
Manager_Name = input("Enter Manager Name:")
Team_Leader_Name = input("Enter Team Leader Name:")
Department = input("Enter Department:")

today = date.today()
print("Today",today)
Age = today.year - DOB

print(" ".join([First_Name,Last_Name]))
print("Date Of Birth:",DOB)
print("AGE:",Age)
print(Employee)
print(Working_Company)
print(Birth_Place)
print(Manager_Name)
print(Team_Leader_Name)
print(Department)
