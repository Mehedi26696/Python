#  1
#  0 0
#  1 1 1
#  0 0 0 0


n=int(input("Enter a number : "))
 
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        if(i%2==0):
            print(0,end=" ")
        else:
            print(1,end=" ")
    print("\n")
