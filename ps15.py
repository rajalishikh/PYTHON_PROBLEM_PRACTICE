# WAP to find the sum of first n numbers. (using while)
user_input=int(input("Please enter a number : "))
x=1
sum=0
while x<=user_input:
    sum=sum+x
  
    x=x+1

print(sum)