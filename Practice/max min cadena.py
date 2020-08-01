def max_min_fun(numbers):
    return str(max([int(num) for num in numbers.split()]))+ ' ' + str(min([int(num) for num in numbers.split()]))

print(max_min_fun('1 3 12 44 -242 -6 5'))