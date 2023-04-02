import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"1.What did you see on line 1?"
"The smallest number is 5 and the largest number is 20."

"2.What did you see on line 2?"
"The smallest number is 3, the largest number is 9;" \
"Row 2 can't generate 4, because it's a multiple of 2, and it only generates odd numbers."

"3.What did you see on line 3?"
"The smallest number is 2.5 and the largest is 5.5" \

"4.code"
print(random.randint(1, 100))
