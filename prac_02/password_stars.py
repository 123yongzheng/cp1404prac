def get_password():
    password = input("Enter password (must be at least 5 characters long): ")
    while len(password) < 5:
        print("Password is too short.")
        password = input("Enter password (must be at least 5 characters long): ")
    return password


def print_password_stars(password):
    print("*" * len(password))


def main():
    password = get_password()
    print_password_stars(password)

main()