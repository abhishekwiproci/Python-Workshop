#a) Print the current date and time at the start of the program (hint: use the datetime library and search the internet)

#b) Print out all the even numbers from the below given list of numbers. Write the solution into a function and have it called in your main block for the requested answer (hint: use loops)

#numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]

import datetime
now = datetime.datetime.now()
print ("Current date and time at the time of program creation is : ")
print ("YY-MM-DD HH:MM:SS")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

numbers = [{'sequence': '952, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]

print (" Even Values from the share List of Dictionary are :")
#print ("Please Print the Entire List of all Numbers :")
#print (numbers)
#print ("Now Please Print all the contents of dictiondary :")
#print (numbers[0]['sequence'])
#print ("Now Please print all only the desired contents of dictionary inside a list :")
#print (numbers[0]['sequence'][3])

l = len(numbers[0]['sequence'])
#l = 10
#print ("no of Letters in ", l)
i = 0
z = 0
for j in range (0, l-1) :
    #x=int(numbers[0]['sequence'][j])
    #print (" value of i is an Integer", numbers[0]['sequence'][j], ord(numbers[0]['sequence'][j]))
    n=ord(numbers[0]['sequence'][j])
    #print (" the value of n is ", n)
    
    if (n >= 48 and n <= 57):
        a = n - 48
        #print ("value of a is", a)
        y = a
        #print ("value of y is", y)
        z=  a + z * 10
        #print ("value of z is", z)
        i = i + 1
        #print ("yes", a)
        x = z % 2
        #print ("the value of x is", x)
    elif (n < 48 or n > 57):
        if ( x == 0 and z!=0 ):
            print (" ", z, end="")
        i = 0 
        z = 0