# Task 1: Sum of Squares
def sum_of_squares(n):
    """
    Calculate the sum of squares of the first `n` natural numbers.
    Example: If n = 3, return 1² + 2² + 3² = 14.
    """
    squares = 0
    for i in range(1,n + 1):
        squares += i ** 2
    return squares

    

# Task 2: Fibonacci Sequence
def fibonacci(n):
    """
    Generate the first `n` numbers in the Fibonacci sequence.
    Return the sequence as a list.
    Example: If n = 5, return [0, 1, 1, 2, 3].
    """
    fib_sequence = []

    
    if n <= 0:
        return fib_sequence
    elif n == 1:
        fib_sequence.append(0)
        return fib_sequence
    elif n == 2:
        fib_sequence.append(0)
        fib_sequence.append(1)
        return fib_sequence


    first = 0
    second = 1


    fib_sequence.append(first)
    fib_sequence.append(second)

    
    for i in range(2, n):
        
        next_fib = first + second

        fib_sequence.append(next_fib)

        
        first = second
        second = next_fib

    return fib_sequence

# Task 3: Prime Number Check
def is_prime(num):
    """
    Check if a number is prime.
    Return True if the number is prime, otherwise False.
    Example: is_prime(7) → True, is_prime(10) → False.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Task 4: Largest Number in List
def find_largest(numbers):
    """
    Find the largest number in a list of numbers.
    Return the largest number.
    Example: find_largest([3, 7, 2, 9]) → 9.
    """
    largest_num = numbers[0]
    for number in numbers:
        if number > largest_num:
            largest_num = number

    return largest_num
        


# Task 5: Reverse a Number
def reverse_number(num):
    """
    Reverse the digits of a number.
    Return the reversed number.
    Example: reverse_number(123) → 321.
    """
    reversed_num = int(str(num)[::-1])
    return  reversed_num

# Task 6: Leap Year Check
def is_leap_year(year):
    """
    Check if a year is a leap year.
    Return True if it is a leap year, otherwise False.
    A leap year is divisible by 4 but not by 100, unless it is also divisible by 400.
    Example: is_leap_year(2000) → True, is_leap_year(1900) → False.
    """
    if year % 4 == 0: 
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                
                else:
                    return False
            else: 
               return True
    
    else:
        return False

# Task 7: Count Vowels
def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in a string.
    Return the count.
    Example: count_vowels("hello") → 2.
    """
    vowels = "aeiou"
    vowel_count = sum(1 for char in text.lower() if char in vowels)
    return vowel_count

# Task 8: Factorial
def factorial(n):
    """
    Calculate the factorial of a number using a while loop.
    Return the factorial.
    Example: factorial(5) → 120.
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Task 9: Grade Calculator
def calculate_grade(score):
    """
    Calculate the grade based on a score:
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: Below 60
    Return the grade as a string.
    Example: calculate_grade(85) → "B".
    """
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"
    

# Task 10: Password Validator
def validate_password(password):
    """
    Validate a password based on the following rules:
    - At least 8 characters long.
    - Contains at least one uppercase letter.
    - Contains at least one lowercase letter.
    - Contains at least one digit.
    - Contains at least one special character (!@#$%^&*).
    Return True if the password is valid, otherwise False.
    Example: validate_password("Pass123!") → True.
    """
    if len(password) < 8:
        return False
    
    # uppercase letter
    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
            break
    
    if not has_uppercase:
        return False
    
    #lowercase letter
    has_lowercase = False
    for char in password:
        if char.islower():
            has_lowercase = True
            break
    
    if not has_lowercase:
        return False
    
    # digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    
    if not has_digit:
        return False
    
    #special character
    has_special = False
    special_characters = "!@#$%^&*"
    for char in password:
        if char in special_characters:
            has_special = True
            break
    
    if not has_special:
        return False
    
    
    return True
