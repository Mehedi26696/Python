#Show smallest factor of a number n (other than 1)

a=int(input("Enter a number : "))
for i in range(2,a+1,1):
    if(a%i==0):
        print(i)
        break


 