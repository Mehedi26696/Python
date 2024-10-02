#WAP to make a calculator that can perform add,subtract,multiply,devide beetween two inputs


a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
op=input("Enter operator : ")
if(op=='+'):
    print(a+b)
elif(op=='-'):
    print(a-b)
elif(op=='*'):
    print(a*b)
elif(op=='/'):
    print(a/b)
 