
from pickle import TRUE

while True:
    First_Name = input("ENter your First name")
    if First_Name =="" or First_Name.isnumeric()==True or First_Name.isalpha()==False:
        print("Please Enter Again")       
    else:
        break
while True:
    Last_Name = input("ENter your Last name")
    if Last_Name=="" or Last_Name.isnumeric()==True or Last_Name.isalpha()==False:
        print("Please Enter Valid Name")
    else:
        break

while True:
    phone_number = (input("Enter Phone Number"))
    if(phone_number=="" or len(phone_number) < 10 or len(phone_number) > 10 or phone_number.isalpha==TRUE):
        print("PLease Enter  agin")
    else:
        break
    
while True:
    Age = (input("Entre The Age"))
    if(Age=="" or len(Age) < 0 or len(Age) > 3 or int(Age)>100):
        print("Please Enter Valid Age")
    else:
        break

while True:
    City = input("Please Enter The City")
    if(City=="" or City.isnumeric()==True):
        print("Please Enter Valid Data")
    else:
        break

while True:    
    salary = float(input("Enter The Salary"))
    if salary<0:
        print("Please Enter The positive salary")
    else:
        break

while True:
    department = input("ENter The Department")
    if department=="":
        print("Department Should Be Blanked")
    else:
        break

print("First_Name:",First_Name)
print("Last Name:",Last_Name)
print("Phone Number:",phone_number)
print("Age:",Age)
print("Salary:",salary)
print("City:",City)
print("Department:",department)



