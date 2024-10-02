#Show all factors of a number n

a=int(input("Enter a number : "))
for i in range(1,a+1,1):
    if(a%i==0):
        print(i)
 