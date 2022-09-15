
def salary():
    global basic_salary
    basic_salary  = int(input("Enter Salary For Employee"))
    print("BASIC_Salary is:",basic_salary)
    
def HRA():
    hra  = (15/100)*basic_salary
    print("HRA OF BASIC SALARY IS:",hra)

def da():
    da = (25/100)*basic_salary
    print("DA of Basic Salary is:",da)

def bonus():
    bonus1 = (10/100) * basic_salary
    print("Bonous of 10% Salary Is:",bonus1)

    