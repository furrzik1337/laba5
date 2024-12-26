for number in range(10, 100):
    tens_digit = number // 10  # первая цифра числа
    ones_digit = number % 10   # вторая цифра числа
    sum_of_digits = tens_digit + ones_digit
    
    if number % sum_of_digits == 0:
        print(number)