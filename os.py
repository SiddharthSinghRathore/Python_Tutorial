import os

print("Present:",os.getcwd())
print(os.getpid())
#os.mkdir(".\\test123")
os.chdir(".\\test123")
print("Present:",os.getcwd())

