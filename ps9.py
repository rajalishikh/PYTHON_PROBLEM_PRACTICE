# Search for a number x in this tuple using loop:
tuple_list=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x=int(input('please gibe me a number: '))
y=0
while y<len(tuple_list):
    
    if x == tuple_list[y]:
        print("yes the number is available in this index",y)
    else:
        print("The number is not available in this tuple")
    y+=1
    
    