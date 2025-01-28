# WAP to find the factorial of first n numbers. (using for)
num=int(input("please enter a number "))
factorial=1


for x in range(1,num+1):
    print(x)
    factorial=factorial*x
print(factorial)
    