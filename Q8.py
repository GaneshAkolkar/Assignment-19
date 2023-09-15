def multiply_list_numbers(input_list):
    result = 1
    for num in input_list:
        result *= num
    return result

# Call the function with a list
my_list = [1, 2, 3, 4, 5]
result = multiply_list_numbers(my_list)
print("Product:", result)
