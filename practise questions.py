#Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.
s = input ("Please Provide how many numbers you want to Compare :")
i = int (s)
l = i
test = []
j = 1
while i > 0:
    print ("Enter the Value", j , "   :", end="")
    test.append(int (input()))
    i = i-1
    j = j +1

i = 0
j = 0
while i < l-1 and j == 0:
    if (test[i] == test[i+1]):
        i = i + 1
    elif (test[i] != test[i+1]):
        j = j +1
if j == 0:
    print ("All Numbers are same")
elif j != 0:
    print ("All the Numbers are not same")


#Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive

s = input ("Please Enter a no. of Your Choice:", )
i = int (s)
l = len (s)

def sumat(i):
    x =0
    for j in range (len (s)):
        x = x + i % 10
        i = i // 10
    #print ("sum", x)
    return x

if i <= 0:
    while i <= 0:
        b= input ("The Value of No. Provided by you either Negative or Zero, Kindly Provide a positive No.")
        i = int (b)

if (i > 0 and i < 10):
    print ("The value of Digit after Substracting its own Digits", i)
    
elif i >= 10:
    while i >= 10 :
        i = i - sumat(i)
    if i <= 10:
        print ("The value of Digit after Substracting its own Digits", i)

    

#Write a Python program to find the digits which are absent in a given mobile number
s = input ("Please Enter Your Mobile no. :", )
i = int (s)
l = len (s)

while (l != 10 or s[0] == '0'):
        s= input ("Mobile No. You Entered is incorrect, Kindly Enter a 10 Digit Mobile No. :")
        i = int (s)
        l = len (s)

r = []
j = 0
while i > 0:
    r.append(i % 10)
    i = i // 10
    j = j +1
    #print ("value of i after division", r, i, r[0])


c = 0
i = 0
z = 0
d = 0
m = 0
print ("Your Mobile No. does not Have following Digits :", end="")
while d < 10:
    c = 0
    i = 0
    z = 0
    while c < 10:
        if (r[i] == d):
            z = z + 1
        elif (r[i] != d):
            m = m + 1
        i = i + 1
        c = c + 1
    if (z <= 0):
        print (d , ", " ,end="")
    d = d + 1
    
import sys
sys.stdout.write('\b \b')
sys.stdout.write('\b \b')

i = int (s)

def sumat(i):
    x =0
    for j in range (len (s)):
        x = x + i % 10
        i = i // 10
    #print ("sum", x)
    return x

if (sumat(i) == 45):
    print (end= "\r")
    print ("'Voila' Your Mobile No. is Unique and is having all the Digits")

#Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

list = ['a', 'e', 'i', 'o', 'u']
i = 0
j = 0
print (list)

print ("Strings with 1 Character")
while i < 5:
    print (list[i], ", ", end="")
    i = i + 1

i = 0
j = 0
print ("Strings with 2 Character")
while i < 5:
    while j < 5:
        print (list[i]+list[j], ", ", end="")
        j = j + 1
    i = i + 1
    j = 0

i = 0
j = 0
k = 0
print ("Strings with 3 Character")
while i < 5:    
    while j < 5:
        while k < 5:
            print (list[i]+list[j]+list[k], ", ", end="")
        k = k + 1
        j = 0
    i = i +1
    j = 0
    k = 0
l = 0    
print ("Strings with 4 Character")
while l < 5:
    while k < 5:    
        while i < 5:
            while j < 5:
                print (list[i]+list[j]+list[k]+list[l] , ", ", end="")
                j = j + 1
            i = i + 1
            j = 0
        k =  k +1
        i = 0
        j = 0
    l = l + 1
    i = 0
    j = 0
    k = 0    


#Write a Python program to find common divisors between two numbers in a given pair.


