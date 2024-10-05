import os
import functions as f
import random as rand

# Welcome message :)
print("Welcome to CatGogh! I hope you have fun :) ")

# Paths for the input images and output folder
initial_image_data = "./data/catgogh"  # Folder holding original images
output_folder = "./output/algo-1"       # Folder to save the generated images to

# Make sure folder exists
try:
    os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist
except OSError as err:
    print(f"Error creating output folder: {err}")
    raise  # If the folder creation fails, raise an exception and stop the program.

# Load images from the input folder
try:
    images_files = f.load_images_from_folder(initial_image_data)  # Load all images from the folder
    if not images_files:
        raise ValueError("No images found in the folder. :/")  # If no images are found, raise error
except (FileNotFoundError, ValueError) as err:
    print(f"Error loading images. Try again :/ : {err}")
    raise  # Stop the program if there are issues loading images

# Lists to hold image halves
desat_overlays = []  # Stores desaturated image halves
plain_overlays = []  # Stores plain normal image halves

# Process each image loaded from the folder
for i, (img, filename) in enumerate(images_files):
    try:
        # Split the image into two halves: left and right
        left, right = f.split_image(img)
        
        # Add plain left and right halves to the plain_overlays list
        plain_overlays.append(left)
        plain_overlays.append(right)

        # Desaturate both halves with a random desaturation level between 0 and 0.5
        desat_left = f.desaturate_image(left, rand.uniform(0, .5))
        desat_right = f.desaturate_image(right, rand.uniform(0, .5))

        # Add desaturated left and right halves to the desat_overlays list
        desat_overlays.append(desat_left)
        desat_overlays.append(desat_right)
    except Exception as err:
        # If an error occurs while processing the image, print an error message and skip the image
        print(f"Error processing image {filename}: {err}")
        continue  # Continue with the next image

total_imgs = 8
remaining_imgs = total_imgs  # Track the number of remaining images to generate

# Generate the combined images
while remaining_imgs > 0: # More intuitive version of a for loop 
    remaining_imgs -= 1  # Decreases the remaining image count

    try:
        # Randomly select one plain half and one desaturated half to combine
        left_half = rand.choice(plain_overlays)
        right_half = rand.choice(desat_overlays)

        # Combine the selected halves into a single image
        sliced_image = f.combine_image_halves(left_half, right_half)

        # Generate a filename for the new image
        random_prefix = rand.randint(1000, 9999)
        output_filename = f"{random_prefix}_mixed_image_{total_imgs - remaining_imgs}.png"
        output_file_path = os.path.join(output_folder, output_filename)  # Full path for the output image

        # Save the new image to the output folder
        f.save_image_to_file(sliced_image, output_file_path)
        print(f"Image saved: {output_file_path}")  # Print a message confirming the image was saved
    except Exception as err:
        # If an error occurs during image generation or saving, print an error message and skip this iteration
        print(f"Error during image generation: {err}")
        continue  # Skip this iteration and proceed with the next image

# Final message: success! 
print("Image generation complete! Check the output folder for your new fabulous images.")