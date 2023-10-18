def hex_to_gray(hex_code):
    # Remove the '#' from the hex code if it exists
    hex_code = hex_code.lstrip('#')

    # Convert the hex code to RGB
    r, g, b = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    # Calculate the grayscale value
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    # Round to nearest integer and return
    return round(gray)

a = hex_to_gray('#414141')

print(a)