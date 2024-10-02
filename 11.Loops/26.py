#Show largest factor of a number n (other than itself)

a=int(input("Enter a number : "))

for i in range(1,a,1):
    if(a%i==0):
        b=i

print(b)      


 