
#        *
#      * *
#    * * *
#  * * * *

#Alternate approach

n=int(input("Enter a number : "))

for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if((i+j)>(n)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n",end="")