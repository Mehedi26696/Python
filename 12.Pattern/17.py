
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# Alternate approach
n=int(input("Enter a number : "))

for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        if((i==j) or ((i+j)%2==0)):
            print(1,end=" ")
        else:
            print(0,end=" ")
 
    print("\n",end="")
