import random

def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    number_scores = int(input("Enter number of scores: "))
    with open("results.txt", "w") as f:
        for i in range(number_scores):
            score = random.randint(0, 100)
            result = get_score_result(score)
            f.write(str(score) + " - " + result + "\n")
main()