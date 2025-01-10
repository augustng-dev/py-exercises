def even_digit_numbers(start, end):
    return ','.join([str(num) for num in range(start, end + 1) if all(int(digit) % 2 == 0 for digit in str(num))])

print(even_digit_numbers(1200, 2010))