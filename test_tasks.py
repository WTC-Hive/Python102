import pytest
from tasks import (
    sum_of_squares,
    fibonacci,
    is_prime,
    find_largest,
    reverse_number,
    is_leap_year,
    count_vowels,
    factorial,
    calculate_grade,
    validate_password,
)

def test_sum_of_squares():
    assert sum_of_squares(3) == 14
    assert sum_of_squares(5) == 55

def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(10) is False
    assert is_prime(2) is True

def test_find_largest():
    assert find_largest([3, 7, 2, 9]) == 9
    assert find_largest([-1, -5, -3]) == -1

def test_reverse_number():
    assert reverse_number(123) == 321
    assert reverse_number(100) == 1

def test_is_leap_year():
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2024) is True

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_calculate_grade():
    assert calculate_grade(85) == "B"
    assert calculate_grade(95) == "A"
    assert calculate_grade(65) == "D"
  
def test_validate_password():
    assert validate_password("Pass123!") is True
    assert validate_password("password") is False
    assert validate_password("12345678") is False
