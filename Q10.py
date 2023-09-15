def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Call the function to check if a number is even or odd
num = 7
result = is_even_or_odd(num)
print(num, "is", result)
