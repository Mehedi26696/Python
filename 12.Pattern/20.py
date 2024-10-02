
#        1
#      1 2
#    1 2 3
#  1 2 3 4

n=int(input("Enter a number : "))

for i in range(1,n+1,1):
    for j in range(1,n+1-i,1):
        print(" ",end=" ")
    for k in range(1,i+1,1):
        print(k,end=" ")
    print("\n",end="")