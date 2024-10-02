#vowel and consonant check

#include <iostream>
 
ch=input("Enter a character : ")
if ((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z')):

     if (ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
        print("Vowel")
     else:
        print("Consonant")
else:
    print("It is not a alphabet")
 