"""
function main()
    get password
    while not is_valid_password(password):
        print invalid
        get password
    print len password

function is_valid_password(password):
    if not MIN_LENGTH<len(password)<MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        if char.islower():
            count_lower+=1
        if char.isupper():
            count_upper+=1
        if char.isdigit():
            count_digit+=1
        if SPECIAL_CHARS_REQUIRED and char in SPECIAL_CHARACTERS:
            count_special+=1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED and count_special == 0:
        return False
    return True
"""

MIN_LENGTH = 5
MAX_LENGTH = 20
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if not MIN_LENGTH < len(password) < MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.islower():
            count_lower += 1
        if char.isupper():
            count_upper += 1
        if char.isdigit():
            count_digit += 1
        if SPECIAL_CHARS_REQUIRED and char in SPECIAL_CHARACTERS:
            count_special += 1
    # print(f"lower:{count_lower}, upper:{count_upper}, digit:{count_digit}, spec:{count_special}")

    # TODO: if any of the 'normal' counts are zero, return False
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if SPECIAL_CHARS_REQUIRED and count_special == 0:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()

