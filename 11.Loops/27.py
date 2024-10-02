# Write a program that prints all prime numbers up to
# x. The integer x will be input to your program.

a=int(input("Enter a number : "))
for i in range(2,a+1,1):
    c=False
    for j in range(2,i,1):
        if(i%j==0):
            c=True
    if(c):
      pass
    else:
        print(i)
 