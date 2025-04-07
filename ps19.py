# WAF to print the elements of a list in a single line. (list is the parameter) 
myFriend=['Arif',"Jihat","Rasel","Nibir","Siam","My best Friend My wife Bushra"]
def find_single_line(a):
    for x in a:
        print(x,end=' ')

find_single_line(myFriend)