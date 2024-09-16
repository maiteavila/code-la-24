import sys
from PIL import Image

# Error Handling
if len(sys.argv) != 3:
    print("Please type python3 'python file name' 'image file name' 'image file name'")
    sys.exit(1)

filename1 = sys.argv[1]
filename2 = sys.argv[2]

try:
    img1 = Image.open(filename1)
    img2 = Image.open(filename2)
except FileNotFoundError:
    print(f"Error: file not found.")
    sys.exit(1)

# Get the sizes of the images
size1 = img1.size
size2 = img2.size

# Resize img2 to match img1 if they are not the same size
if size1 != size2:
    img2 = img2.resize(size1)  # Resize image 2 to match the size of image 1

# Blend images
blended_img = Image.blend(img1,img2,0.5)

# Save the blended image'
new_filename = "blended-" + filename1
blended_img.save(new_filename)

print(f"Images blended and saved as '{new_filename}'")
