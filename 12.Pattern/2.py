# NUmber square
 
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

n=int(input("Enter a number : "))

for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        print(j,end="")
    print("\n",end="")
