"""print("Hello World", end=",")
print("Hello")
"""

x = open("demo.txt","w")
print("Hello World",file = x)
x.close()