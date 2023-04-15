def extract_name(email):
    parts = email.split('@')
    name_part = parts[0]
    name_words = name_part.split('.')
    name_words = [word.title() for word in name_words]
    return ' '.join(name_words)

emails = {}

while True:
    email = input("Email: ")
    if email == "":
        break
    name = extract_name(email)
    response = input(f"Is your name {name}? (Y/n) ")
    if response == "" or response.lower() == "y":
        emails[email] = name
    else:
        name = input("Name: ")
        emails[email] = name

for email, name in emails.items():
    print(f"{name} ({email})")
