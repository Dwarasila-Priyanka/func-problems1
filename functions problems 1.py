# 1.Print numbers from 1 to N
def print_numbers(n):
    for i in range(1, n+1):
        print(i, end=' ')

print_numbers(10)

#2.Print even numbers up to N
def print_even(n):
    for i in range(2, n+1, 2):
        print(i, end=' ')

print_even(10)

#3.Sum of first N natural numbers
 def sum_natural(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(sum_natural(10))

#4.Check if number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True

#5.Print all prime numbers up to N
def primes_upto_n(n):
    for i in range(2, n+1):
        if is_prime(i):
            print(i, end=' ')

primes_upto_n(20)

#6.Count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

print(count_digits(12345))  # 5

#7. Reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

print(reverse_number(1234))  # 4321

#8.Check if number is palindrome
def is_palindrome_number(num):
    return num == reverse_number(num)

print(is_palindrome_number(121))  # True

#9.Sum of digits
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(sum_of_digits(1234))  # 10

#10. Check Armstrong number
def is_armstrong(n):
    power = count_digits(n)
    temp = n
    result = 0
    while temp > 0:
        digit = temp % 10
        result += digit ** power
        temp //= 10
    return result == n

print(is_armstrong(153))  # True

#11.Multiplication table of a number
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

multiplication_table(5)

#12.Find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(12, 18))  # 6

#13.Check leap year
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_leap(2020))  # True

#14. Print Fibonacci series up to N terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(10)

#15.Find factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print(factorial(5))  # 120

#16. Count even and odd digits
def count_even_odd_digits(n):
    even = odd = 0
    while n > 0:
        if n % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        n //= 10
    return even, odd

print(count_even_odd_digits(123456))  # (3, 3)

#17. Print all factors of a number
def print_factors(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=' ')

print_factors(12)

#18. Check perfect number

def is_perfect(n):
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n

print(is_perfect(28))  # True




