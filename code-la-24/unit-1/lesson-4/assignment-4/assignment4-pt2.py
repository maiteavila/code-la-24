import sys
from PIL import Image, ImageFilter

# #Version 1
# if len(sys.argv) != 5:
#     exit("This program requires four arguments")

# # Open images
# images = [Image.open(arg) for arg in sys.argv[1:]]

# # Create a new blank image with a white background
# collage_width = 600
# collage_height = 600
# collage = Image.new("RGB", (collage_width, collage_height), (255, 255, 255))

# # Calculate positions for each image
# positions = [(0, 0), (300, 0), (0, 300), (300, 300)]

# for i, img in enumerate(images):
#     # Resize each image to cover half of the collage space
#     img = img.resize((300, 300), Image.LANCZOS)
#     collage.paste(img, positions[i])

# collage.save("assignment-4/collage-1.jpg")


# #Version 2
# if len(sys.argv) != 5:
#     exit("This program requires four arguments")

# # Open images
# images = [Image.open(arg) for arg in sys.argv[1:]]

# # Create a new blank image with a white background
# collage_width = 600
# collage_height = 600
# collage = Image.new("RGBA", (collage_width, collage_height), (255, 255, 255, 0))

# # Calculate positions for each image
# positions = [(0, 0), (150, 150), (300, 0), (450, 150)]

# for i, img in enumerate(images):
#     # Resize images for collage
#     img = img.resize((300, 300), Image.LANCZOS)
    
#     # Distortion 
#     if i % 2 == 0:  # Apply distortion to every other image
#         img = img.filter(ImageFilter.GaussianBlur(radius=5))

#     # Set transparency for layering
#     transparency = 128 if i % 2 == 0 else 180  
#     img.putalpha(transparency)

#     # Paste the image onto the collage
#     collage.paste(img, positions[i], img)

# # Save the collage
# collage.save("assignment-4/collage-2.png")