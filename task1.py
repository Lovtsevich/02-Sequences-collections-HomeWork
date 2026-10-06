# список numbers = [15, 7, 28, 10, 21]
numbers = [15, 7, 28, 10, 21]
maxNumber = max(numbers)
while maxNumber in numbers:
    numbers.remove(maxNumber)

maxNumber = max(numbers)
print(maxNumber)

# список numbers = [4, 6, 2, 11, 1, 11, 5, 11, 7]
numbers = [4, 6, 2, 11, 1, 11, 5, 11, 7]
maxNumber = max(numbers)
while maxNumber in numbers:
    numbers.remove(maxNumber)

maxNumber = max(numbers)
print(maxNumber)