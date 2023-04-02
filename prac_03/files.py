name = input("Enter your name: ")
with open('name.txt', 'w') as name_file:
    name_file.write(name)
with open('name.txt', 'r') as name_file:
    name = name_file.read().strip()
print(f"Your name is {name}")

with open('numbers.txt', 'r') as numbers_file:
    number1 = int(numbers_file.readline())
    number2 = int(numbers_file.readline())
print(number1 + number2)

total = 0
with open('numbers.txt', 'r') as numbers_file:
    for line in numbers_file:
        number = int(line.strip())
total += number

print(total)