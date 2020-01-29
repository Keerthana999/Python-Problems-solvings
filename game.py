rock=1
paper=2
scissors=3
n=int(input("enter 1 or 2 or 3:"))
import random
z=random.randrange(1,3)

print(z)
if(n==rock and z==1):
 print("It is a draw")
elif(n==rock and z==2):
    print("paper wins")
elif(n==rock and z==3):
    print("rock wins")
elif(n==paper and z==1):
    print("paper wins")
elif(n==paper and z==2):
    print("It ia a draw")
elif(n==paper and z==3):
    print("scissors win")
elif(n==scissors and z==1):
    print("rock wins")
elif(n==scissors and z==2):
    print("scissors win")
elif(n==scissors and z==3):
    print("it is a draw")

    
 
