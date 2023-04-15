"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformatting the dictionary to follow PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

print(CODE_TO_NAME)

while True:
    state_code = input("Enter state code: ").upper()  # Converting input to uppercase
    try:
        state_name = CODE_TO_NAME[state_code]
    except KeyError:
        print("Invalid state code")
    else:
        print(f"{state_code} is {state_name}")

    if state_code == "":
        break
