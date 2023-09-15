def is_in_range(number, start, end):
    return start <= number <= end

# Call the function to check if a number is in the range [1, 10]
num = 5
if is_in_range(num, 1, 10):
    print(num, "is in the range [1, 10]")
else:
    print(num, "is not in the range [1, 10]")
