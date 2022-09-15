import re

# +603-007 1212, +6099.100 3344, 017-99988800.
pattern = re.compile(r'(\+\d)?\d{3}[.-]\d{3}\s?\d{4}')
matches = pattern.finditer("+6099.100 3344")
for match in matches:
    # print(match.group())
     with open("pat1.txt",'a+') as file1:
     #f = open("pat.tx","w+")
        file1.write(match.group())
        print(file1.read())

file1.close()