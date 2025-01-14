import os


## Transform the image format that is matched name

## Path to the folder containing the files
workspace = 'F:\Download\BLSBookDetailStyle'
# Files that need to be renamed folder
old_folder = workspace + '\Images'
# Renamed image folder
new_folder = workspace + '\FormatedImages\qrcode'
new_folder2 = workspace + '\FormatedImages\cover'
# Flie name suffix
suffix = '_二维码.'

# Transform the image format that is matched name to png in the current folder is not recursive
# and the rest of the image format to jpg
# and replace the original image to new folder
for file in os.listdir(old_folder):
    if suffix in file:
        print(file)

print('Transform the image format that is matched name to png successfully!')