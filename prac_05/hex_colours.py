COLOR_TO_CODE = {"ALICEBLUE": "#f0f8ff",
                 "ANTIQUEWHITE": "#faebd7",
                 "AQUA": "#00ffff",
                 "BEIGE": "#f5f5dc",
                 "BISQUE": "#ffe4c4",
                 "BLUEVIOLET": "#8a2be2",
                 "CHOCOLATE": "#d2691e",
                 "CORAL": "#ff7f50",
                 "DARKGREEN": "#006400",
                 "FUCHSIA": "#ff00ff"}

while True:
    color_name = input("Enter a color name: ").upper()
    if color_name == "":
        break
    try:
        color_code = COLOR_TO_CODE[color_name]
    except KeyError:
        print("Invalid color name")
    else:
        print(f"{color_name} is {color_code}")

