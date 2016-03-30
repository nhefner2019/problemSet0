from math import factorial

#Problem 0

'''def even_odd(number):
	
	if number % 2 == 0:
		return True
	else:
		return False
		
#----------Main Program-------------
number = int(raw_input("What is your number? "))

numb = even_odd(number)

print(numb)'''


#Problem 1

'''def number_digits(number):
	
	digits = len(number)
	
	return digits
	
#------------main program------------
number = raw_input("What is your number? "))

numb = number_digits(number)

print("Your number has {} digits.".format(numb))'''


#Problem 2

'''def sum_digits(number):
	sum = 0
	for digit in number:
		sum += int(digit)
	return sum
		
#--------------Main Program----------------

number = raw_input("What is your number? ")
sum = sum_digits(number)
print("The sum of your digits is {}." .format(sum))'''
		

#Problem 3

'''def sum_less_ints(number):
	sum = 0
	ints = range(number)
	
	for integer in ints:
		sum += integer
	
	return sum
	
#-------------Main Program------------
number = int(raw_input("What is your number? "))

sum = sum_less_ints(number)

print("The sum of the integers less than {} is {}.".format(number, sum))'''

#Problem 4

'''def number_factorial(number):
	
	factor = factorial(number)
	
	return factor

#--------Main Program------------
number = int(raw_input("What is your number? "))

factor = number_factorial(number)

print("The factorial of {} is {}." .format(number, factor))'''


#Problem 5

'''def possible_factors(dividend, divisor):

	if dividend % divisor == 0:
		return True
	else:
		return False
		
#-------------Main Program-------------
dividend = int(raw_input("What will be your dividend? "))
divisor = int(raw_input("What will be your divisor? "))

quotient = possible_factors(dividend, divisor)

print(quotient)'''

#Problem 6

'''def prime_number(number):

	numberRange = range(2, number)
	
	for integer in numberRange:
		while number % integer == 0:
			return True
			
		return False

#-----------Main Program--------------
number = int(raw_input("What is your number? "))

result = prime_number(number)

print(result)'''



		
	
		