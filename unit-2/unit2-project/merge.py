import os

# Define the folder path 
folder_path = 'debut-scrape'
# Define the output file name
output_file = 'debut-songs.txt'

# Open the output file
with open(output_file, 'w') as outfile:
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Only process .txt files
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            # Open each file and write its content to the output file
            with open(file_path, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')  # Add a newline to separate contents of each file



# Define the folder path 
folder_path = 'ttpd-scrape'
# Define the output file name
output_file = 'ttpd-songs.txt'

# Open the output file
with open(output_file, 'w') as outfile:
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Only process .txt files
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            # Open each file and write its content to the output file
            with open(file_path, 'r') as infile:
                outfile.write(infile.read())
                outfile.write('\n')  # Add a newline to separate contents of each file


