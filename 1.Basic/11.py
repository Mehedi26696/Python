# Take two integers input, a and b : a>b, and find the
# remainder when a is divided by b.



a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

c=a//b
print(c)
d=a-(b*c)
print("Remainder : ",d)

 