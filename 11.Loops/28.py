# Write a program that prints all prime factors of a
# number n given as input.

n=int(input("Enter a number : "))
a=False
for i in range(2,n,1):
    if(n%i==0):
        for j in range(2,i,1):
            if(i%j==0):
                a=True
        if(a):
            pass
        else:
            print(i)
 