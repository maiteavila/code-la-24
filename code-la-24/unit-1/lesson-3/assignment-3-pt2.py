import sys
from PIL import Image

# Error Handling

user_did_input_three_variables= len(sys.argv) != 3

if not user_did_input_three_variables:
    print("Please type python3 'python file name' 'image file name' 'rotation angle")
    sys.exit(1)

filename = sys.argv[1]

try:
    img = Image.open(filename)
except FileNotFoundError:
    print(f"Error: file not found.")
    sys.exit(1)

try:
    # Convert the second argument (rotation angle) to an integer with 'int'
    angle = int(sys.argv[2])
except ValueError:
    print(f"Error: Not a valid number.")
    sys.exit(1)

# Rotate the image by the specified angle
rotated_img = img.rotate(angle)

# Save the rotated image with a new name, prefixed with 'rotated-'
new_filename = "rotated-" + filename
rotated_img.save(new_filename)

print(f"Image rotated by {angle} degrees and saved as '{new_filename}'")