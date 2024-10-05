import os
import random
from PIL import Image, ImageEnhance, ImageFilter

# Welcome message :)
print("Welcome to CatGogh! I hope you have fun :) ")

# Paths for the input images and output folder
image_folder = "./data/catgogh" # Folder holding original images
output_folder = "./output/algo-2" # Folder to save the generated images to

# Make sure folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List of the images in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

def save_image_to_file(image, file_path):
    """Saves the given image to the specified file path."""
    image.save(file_path)

# Opens a random image from the folder
def get_random_image():
    img_name = random.choice(image_files)
    img_path = os.path.join(image_folder, img_name)
    return Image.open(img_path)

# Saturation
def adjust_saturation(image, factor=3.0):
    enhancer = ImageEnhance.Color(image)
    return enhancer.enhance(factor)

# Gaussian blur
def apply_gaussian_blur(image, radius=5):
    return image.filter(ImageFilter.GaussianBlur(radius))

# Combine two images
def combine_images(image1, image2):
    return Image.blend(image1, image2, alpha=0.5)

# Create a new image
def generate_new_image(output_file_path):
    # Select two random images from the folder
    img1 = get_random_image()
    img2 = get_random_image()

    # Resize images to be the same size
    img2 = img2.resize(img1.size)

    # Adjust saturation of both images
    img1 = adjust_saturation(img1, factor=random.uniform(1.2, 2.0))
    img2 = adjust_saturation(img2, factor=random.uniform(1.2, 2.0))

    # Apply Gaussian blur to one or both images
    if random.choice([True, False]):
        img1 = apply_gaussian_blur(img1, radius=random.randint(1, 10))
    if random.choice([True, False]):
        img2 = apply_gaussian_blur(img2, radius=random.randint(1, 10))

    # Combine the two images
    new_image = combine_images(img1, img2)

    # Save the result
    new_image.save(output_file_path)

# Execution block
total_imgs = 8
remaining_imgs = total_imgs

for i in range(total_imgs):
    random_prefix = random.randint(1000, 9999)
    output_filename = f"{random_prefix}_mixed_image_{i + 1}.png"
    output_file_path = os.path.join(output_folder, output_filename)

    # Generate and save the new image
    generate_new_image(output_file_path)

    # Final message: success! 
print("Image generation complete! Check the output folder for your new fabulous images.")