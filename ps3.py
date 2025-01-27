# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value
marks={}
user=int(input("please Enter your  marks " ))
marks.update({'phy':user})
user=int(input("please Enter your  marks " ))
marks.update({'cha':user})
user=int(input("please Enter your subject and marks " ))
marks.update({'math':user})
print(marks)


