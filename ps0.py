from math import factorial

#Problem 0

def even_odd(number):
	'''determines if a number is even or odd'''
	
	if number % 2 == 0:
		return True
	else:
		return False


#Problem 1

def number_digits(number):
	'''determines how many digits a number has'''
	
	digits = len(str(number))
	
	return digits


#Problem 2

def sum_digits(number):
	'''determines the sum of a number's digits'''
	
	sum = 0
	number = str(number)
	for digit in number:
		sum += int(digit)
	return sum
		

#Problem 3

def sum_less_ints(number):
	'''determines the sum of all integers less than the number'''
	
	sum = 0
	ints = range(number)
	
	for integer in ints:
		sum += integer
	
	return sum
	

#Problem 4

def number_factorial(number):
	'''determines the factorial of a number'''
	
	factor = factorial(number)
	
	return factor



#Problem 5

def possible_factors(dividend, divisor):
	'''determines if one number is a factor of another'''
	if dividend % divisor == 0:
		return True
	else:
		return False
		
#Problem 6

def prime_number(number):
	'''determines if a number is prime'''
	
	numberRange = range(2, number)
	
	for integer in numberRange:
		while number % integer == 0:
			return False
			
		return True
		
#Problem 7

def perfect_number(number):
	'''determines if a number is perfect'''
	
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
	'''determines if the sum of a number's digits is a factor of the original number'''
	
	sum = sum_digits(number)
	
	if number % sum == 0:
		return True
	else:
		return False



