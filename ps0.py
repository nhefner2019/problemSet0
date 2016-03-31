from math import factorial

#Problem 0

def even_odd(number):
	
	if number % 2 == 0:
		return True
	else:
		return False


#Problem 1

def number_digits(number):
	
	digits = len(str(number))
	
	return digits


#Problem 2

def sum_digits(number):
	sum = 0
	number = str(number)
	for digit in number:
		sum += int(digit)
	return sum
		

#Problem 3

def sum_less_ints(number):
	sum = 0
	ints = range(number)
	
	for integer in ints:
		sum += integer
	
	return sum
	

#Problem 4

def number_factorial(number):
	
	factor = factorial(number)
	
	return factor



#Problem 5

def possible_factors(dividend, divisor):

	if dividend % divisor == 0:
		return True
	else:
		return False
		
#Problem 6

def prime_number(number):

	numberRange = range(2, number)
	
	for integer in numberRange:
		while number % integer == 0:
			return False
			
		return True
		
#Problem 7

def perfect_number(number):

	numberRange = range(1, number)
	
	sum = 0
	
	for integer in numberRange:
		if number % integer == 0:
			sum += integer
			
	if sum == number:
		return True
	else:
		return False
			
#Problem 8

def sum_divisible(number):
	
	sum = sum_digits(number)
	
	if number % sum == 0:
		return True
	else:
		return False



