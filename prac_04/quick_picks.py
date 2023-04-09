import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6
NUM_QUICK_PICKS = int(input("How many quick picks? "))

for i in range(NUM_QUICK_PICKS):
    numbers = random.sample(range(MIN_NUMBER, MAX_NUMBER+1), NUMBERS_PER_QUICK_PICK)
    print(" ".join("{:2}".format(n) for n in sorted(numbers)))
