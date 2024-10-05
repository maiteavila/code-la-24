
# This contains all the main functions
import os
from PIL import Image, ImageEnhance

def crop_to_height(image, target_height):
    # If the image is already the target height, return it as is
    if image.height == target_height:
        return image
    
    # Calculate the cropping region (center crop)
    top = (image.height - target_height) // 2
    bottom = top + target_height
    return image.crop((0, top, image.width, bottom))

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(folder, filename)
            try:
                img = Image.open(img_path)
                images.append((img, filename))  # Store both image and filename
            except IOError:
                print(f"Unable to load image: {filename}")
    return images

def desaturate_image(image, factor=0):
    
    # Create a Color enhancer
    enhancer = ImageEnhance.Color(image)
    
    desaturated_image = enhancer.enhance(factor)
    
    return desaturated_image


def split_image(image):
    width, height = image.size
    
    mid = width // 2 # Calculate the midpoint, using "//" to round down 
    
    left_half = image.crop((0, 0, mid, height)) # Create the left half
    
    right_half = image.crop((mid, 0, width, height)) # Create the right half
    
    return left_half, right_half


# Function to combine two image halves with height adjustment
def combine_image_halves(left_half, right_half):
    
    min_height = min(left_half.height, right_half.height) # Find the minimum height between the two images
    
    # Crop both images to the minimum height
    left_half_cropped = crop_to_height(left_half, min_height)
    right_half_cropped = crop_to_height(right_half, min_height)
    
    # Create a new image with the combined width and the minimum height
    new_width = left_half_cropped.width + right_half_cropped.width
    new_image = Image.new('RGB', (new_width, min_height))
    
    # Paste the left and right halves
    new_image.paste(left_half_cropped, (0, 0))
    new_image.paste(right_half_cropped, (left_half_cropped.width, 0))

    return new_image


def save_image_to_file(image, output_path):
    image.save(output_path)

    print(f"Image saved: {output_path}")