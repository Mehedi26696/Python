# 1
# 1 3
# 1 3 5
# 1 3 5 7

n=int(input("Enter a number : "))

for i in range(1,n+1,1):
    for j in range(1,2*i+1,1):
        if(j%2!=0):
             print(j,end=" ")  
    print("\n",end="")