def get_valid_score():
    while True:
        try:
            score = int(input("Enter a valid score (0-100 inclusive): "))
            if score < 0 or score > 100:
                print("Invalid score, please try again.")
            else:
                return score
        except ValueError:
            print("Invalid input, please enter a number.")

def print_result(score):
    if score >= 90:
        print("Your grade is an A.")
    elif score >= 80:
        print("Your grade is a B.")
    elif score >= 70:
        print("Your grade is a C.")
    elif score >= 60:
        print("Your grade is a D.")
    else:
        print("Your grade is an F.")


def show_stars(score):
    print("*" * score)


def main():
    print("Welcome to the Score Program!")
    while True:
        print("Choose an option:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input(">").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
main()