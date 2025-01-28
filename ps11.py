# Search for a number x in this tuple using loop:
list=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
number_search=int(input('please enter your number: '))
idx=0

for i in list:
  
    
    if(i==number_search):
        print(idx)
        break
    idx=idx+1

  
          


    
