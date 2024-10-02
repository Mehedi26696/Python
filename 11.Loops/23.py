# // Armstrong number example: 153=(1*1*1)+(5*5*5)+(3*3*3)
# // print all armstrong numbers between 1 to 500

for i in range(1,500):
    
    a=i
    b=0
    while a>0 :
        c=a%10
        b+=c*c*c
        a=a//10
    
    if(b==i):
        print(i)
    i+=1

            

 