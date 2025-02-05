import os
import csv

## append mapping and mapping2
## continuing the index

mapping_des = "F:\Download\BLSBookDetailStyle\mapping.csv"
mapping_book = "F:\Download\BLSBookDetailStyle\mappingbook.csv"
mapping_video = "F:\Download\BLSBookDetailStyle\mappingvideo.csv"
mapping_image = "F:\Download\BLSBookDetailStyle\mappingimage.csv"
mapping_audio = "F:\Download\BLSBookDetailStyle\mappingaudio.csv"

index = 0

# copy the mapping to mapping_des with new index
# Init line 1
with open(mapping_des, 'w', encoding='utf-8') as f:
    f.write("INDEX,ID,TYPE,NAME,AUTHOR,PRESS,DESCRIPTION\n")

# Do copy from mapping_book to mapping_des without source row 1
with open(mapping_book, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'INDEX':
            continue
        index += 1
        with open(mapping_des, 'a', encoding='utf-8') as f:
            f.write(f"{index},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}\n")

# Do copy from mapping_video to mapping_des without source row 1
with open(mapping_video, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'INDEX':
            continue
        index += 1
        with open(mapping_des, 'a', encoding='utf-8') as f:
            f.write(f"{index},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}\n")

# Do copy from mapping_image to mapping_des without source row 1
with open(mapping_image, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'INDEX':
            continue
        index += 1
        with open(mapping_des, 'a', encoding='utf-8') as f:
            f.write(f"{index},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}\n")

# Do copy from mapping_audio to mapping_des without source row 1
with open(mapping_audio, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'INDEX':
            continue
        index += 1
        with open(mapping_des, 'a', encoding='utf-8') as f:
            f.write(f"{index},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}\n")
            

print(f"Done! Total {index} lines appended to {mapping_des}")
