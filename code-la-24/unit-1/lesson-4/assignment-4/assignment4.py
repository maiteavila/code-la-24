import os
from PIL import Image

# # Version 1
# # Create a new 400x400 image
# img = Image.new("RGB", (400, 400))

# # Create a simple modulo pattern
# for y in range(400):
#     for x in range(400):
#         pixel = (x % 255, y % 255, (x + y) % 255)
#         img.putpixel((x, y), pixel)

# # Save the image in the assignment-4 folder
# img.save("assignment-4/new-image1.png")


# #Version 2
# # Create a new 400x400 image
# img = Image.new("RGB", (400, 400))

# for y in range(400):
#     for x in range(400):
#         # Create vertical stripes with different colors
#         r = (x % 255)  
#         g = (y % 255) 
#         b = 255 - (x % 255) 
#         pixel = (r, g, b)
#         img.putpixel((x, y), pixel)

# img.save("assignment-4/new-image2.jpg")


# # Version 3
# # Create a new 400x400 image
# img = Image.new("RGB", (400, 400))

# for y in range(400):
#     for x in range(400):
#         # Checkerboard pattern
#         if (x // 50) % 2 == (y // 50) % 2:
#             pixel = (255, 255, 255)
#         else:
#             pixel = (0, 0, 0)
#         img.putpixel((x, y), pixel)

# img.save("assignment-4/new-image3.jpg")