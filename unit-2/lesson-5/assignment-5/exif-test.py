from os import listdir, path
from PIL import Image, ExifTags

files = listdir("./photos")
img = Image.open(path.join("photos", "photo2.jpeg"))
exifData = img.getexif()

print(exifData)
for key in img.getexif().keys():
    print(key, ExifTags.TAGS[key])

#This was pretty straightforward to work with. I was a little confused on how to read some of the output. Some of my photos also ended up having no exif data, at least I think so because it only outputed  a "[]" 