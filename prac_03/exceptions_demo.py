"Questions："
"1.When will a ValueError occur?"
"If there's A number, there's A"

"2.When will a ZeroDivisionError occur?"
"If the input is 0, the output is A"

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError as error:
    print(error)
print("Finished.")