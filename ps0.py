from math import factorial

#Problem 0
#determines if a number is even or odd
def even_odd(number):
	
	if number % 2 == 0:
		return True
	else:
		return False


#Problem 1
#determines how many digits a number has
def number_digits(number):
	
	digits = len(str(number))
	
	return digits


#Problem 2
#determines the sum of a number's digits
def sum_digits(number):
	sum = 0
	number = str(number)
	for digit in number:
		sum += int(digit)
	return sum
		

#Problem 3
#determines the sum of all integers less than the number
def sum_less_ints(number):
	sum = 0
	ints = range(number)
	
	for integer in ints:
		sum += integer
	
	return sum
	

#Problem 4
#determines the factorial of a number
def number_factorial(number):
	
	factor = factorial(number)
	
	return factor



#Problem 5
#determines if one number is a factor of another
def possible_factors(dividend, divisor):

	if dividend % divisor == 0:
		return True
	else:
		return False
		
#Problem 6
#determines if a number is prime
def prime_number(number):

	numberRange = range(2, number)
	
	for integer in numberRange:
		while number % integer == 0:
			return False
			
		return True
		
#Problem 7
#determines if a number is perfect
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
#determines if the sum of a number's digits is a factor of the original number
def sum_divisible(number):
	
	sum = sum_digits(number)
	
	if number % sum == 0:
		return True
	else:
		return False



