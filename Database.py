
from pickle import TRUE
import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="Sid@1996",
        host="localhost",
        port=3306,
        database="employee_lilly"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
conn.autocomit=TRUE


'''cur.execute("CREATE DATABASE EMPLOYEE_LILLY")
cur.execute("SHOW DATABASES")
for x in cur:
  print(x)'''

try:
  cur.execute("CREATE TABLE customers(first_name VARCHAR(255),last_name VARCHAR(255),phone_number VARCHAR(255),Age int(10),city varchar(100),salary int,department varchar(100))");
except Exception as e:
  print(e)

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


cur.execute("""INSERT INTO customers(first_name,last_name,phone_number,Age,city,salary,department) VALUES(?,?,?,?,?,?,?)""",(First_Name,Last_Name,phone_number,Age,City,salary,department))
#cur.execute("""INSERT INTO customers (first_name,last_name,phone_number,Age,city,salary,department) values("sid","rat",123456,22,"pune",1234,"IDS")""")
conn.commit()

print(cur.rowcount, "record inserted.")

