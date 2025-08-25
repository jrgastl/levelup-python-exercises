'''
Author Notes:
In the first attempt, the approach was to find the prime numbers first and then look up for the factors, iterating with a while loop, so the multiplication of the factors would result in the value given in the function.
After checking the instructor solution, I realized the code could be implemented in a much simpler way, looking for the factors from 2 upwards, and then checking if the number was prime.
There is a lot of similarities still though, and I even built a small test in the end to check the result.
'''
from random import randint

def is_prime(value):
    if value <= 1:
        return False
    for x in range(2, value):
        if value % x == 0:
            return False
    return True

def get_prime_factors(number):
    prime_numbers = [y for y in range(2, number) if is_prime(y)]
    prime_factors = []
    dividend = number
    if is_prime(number) == False and number > 1 and type(number) == int:
        while dividend > 1:       
            for n in prime_numbers:
                if dividend % n == 0:
                    prime_factors.append(n)
                    dividend /= n
            prime_factors.sort()          
    else:
        if number > 1 and type(number) == int:
            prime_factors.append(number)
        else:
            return "Number must be bigger than 1 and an integer"

    return prime_factors
    
def test_result(factors):
    result = 1
    for num in factors:
        result *= num
    return result
        

# Please, uncomment the lines below to execute the code with the example given

# r = randint(2,10000)
# result = get_prime_factors(r)
# tested_result = test_result(result)
# print(f'For the number {r} the prime factors are {result}')
# if r == tested_result:
#     print("Result is valid!")
# else:
#     print("Result is not valid!")
