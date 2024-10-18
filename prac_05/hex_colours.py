COLOURS_TO_CODE = {"aliceblue": "#f0f8ff", "black": "#000000", "blue1": "#0000ff", "teal": "#008080",
                     "yellow": "#ffff00", "violet": "#ee82ee", "turquoise": "#40e0d0", "tan": "#d2b48c",
                        "thistle": "#d8bfd8", "tomato": "#ff6347"}

print(COLOURS_TO_CODE)

colour_name = input("Enter colour name: ").lower()

while colour_name != "":
    if colour_name in COLOURS_TO_CODE:
        print(f"{colour_name} is {COLOURS_TO_CODE[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()