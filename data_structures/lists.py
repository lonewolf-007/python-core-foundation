numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("First element:", numbers[0])

numbers.append(60)
print("After append:", numbers)

numbers.remove(20)
print("After remove:", numbers)

for num in numbers:
    print("Number:", num)
