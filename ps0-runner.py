import ps0

#Test cases for Problem 0
print("The number {} is even: {}.".format(4,ps0.even_odd(4)))
print("The number {} is even: {}. \n".format(5,ps0.even_odd(5)))

#Test cases for Problem 1
print("Your number is {}. There is {} digit in {}.".format(1,ps0.number_digits(1),1))
print("Your number is {}. There are {} digits in {}.".format(55,ps0.number_digits(55),55))
print("Your number is {}. There are {} digits in {}.\n".format(4875,ps0.number_digits(4875),4875))

#Test cases for Problem 2
print("Your number is {}. The sum of the digits in {} is {}.".format(23,23,ps0.sum_digits(23)))
print("Your number is {}. The sum of the digits in {} is {}.".format(458,458,ps0.sum_digits(458)))
print("Your number is {}. The sum of the digits in {} is {}.\n".format(1125,1125,ps0.sum_digits(1125)))

#Test cases for Problem 3
print("Your number is {}. The sum of all the integers less than {} are {}.".format(3,3,ps0.sum_less_ints(3)))
print("Your number is {}. The sum of all the integers less than {} are {}.".format(6,6,ps0.sum_less_ints(6)))
print("Your number is {}. The sum of all the integers less than {} are {}.\n".format(10,10,ps0.sum_less_ints(10)))

#Test cases for Problem 4
print("Your number is {}. The factorial of {} is {}, or {}!.".format(2,2,ps0.number_factorial(2),2))
print("Your number is {}. The factorial of {} is {}, or {}!.".format(4,4,ps0.number_factorial(4),4))
print("Your number is {}. The factorial of {} is {}, or {}!.\n".format(5,5,ps0.number_factorial(5),5))

#Test cases for Problem 5
print("Your dividend is {}. Your divisor is {}. {} is a factor of {}: {}.".format(8,2,2,8,ps0.possible_factors(8,2))) 
print("Your dividend is {}. Your divisor is {}. {} is a factor of {}: {}.\n".format(7,2,2,7,ps0.possible_factors(7,2))) 

#Test cases for Problem 6
print("Your number is {}. The number {} is a prime number: {}.".format(5,5,ps0.prime_number(5)))
print("Your number is {}. The number {} is a prime number: {}.\n".format(12,12,ps0.prime_number(12)))

#Test cases for Problem 7
print("Your number is {}. The number {} is perfect: {}.".format(6,6,ps0.perfect_number(6)))
print("Your number is {}. The number {} is perfect: {}.\n".format(4,4,ps0.perfect_number(4)))

#Test cases for Problem 8
print("Your number is {}. The number {} is divisible by the sum of its digits: {}.".format(18,18,ps0.sum_divisible(18)))
print("Your number is {}. The number {} is divisible by the sum of its digits: {}.".format(23,23,ps0.sum_divisible(23)))