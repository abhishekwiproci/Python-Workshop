"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi

print (value of Pi is 'pi')
print (Type of Pi is 'math.pi')


# TODO: Write a conditional to print out if `i` is less than or greater than 50

i = random.randint(0, 100)

Print ("value of i is " 'i')

if i < 50:
	print("I is less than fifty")
	else i > 50:
		print("I is greater than fifty")


# TODO: Write a conditional that prints the color of the picked fruit


picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == "orange":
	print(" Picked Fruit is Orange")
	elif picked_fruit == "strawberry":
		print("Picked Fruit is strawberry")
	else:
		print ("Picked Fruit is banana")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

def multiply (num1, num2):
	num3 = num1*num2
	return num3
print("12 x 96 =", multiply(12,96))
print("48 x 17 =", multiply(48,17))
print("196523 x 87323 =", multiply (196523, 87323))

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",)

print("48 x 17 =",)

print("196523 x 87323 =",)

print ("Lab 1 Completed")
