import os
import shutil
import pandas as pd

## Store the new line in the csv file from adding excel file

# Added excel file
origin_excel = "F:\Download\BLSBookDetailStyle\艺术鉴赏大屏展示数据 2024.12.20.xlsx"

# Added file path
added_file_path = "F:\\Download\\BLSBookDetailStyle\\Images\\added"

# Destination mapping csv file
destination_csv = "F:\Download\BLSBookDetailStyle\mapping.csv"

# Read excel file
datas = pd.read_excel(origin_excel, usecols=[0,1,2,3,4], dtype=str) ## Read the first 5 columns to string

# Get dest index,which is the last index in A column
mapping_index = pd.read_csv(destination_csv, usecols=[0], dtype=str)
mapping_index = mapping_index['INDEX'].tolist()
mapping_index = int(mapping_index[-1]) + 1

# Obtain images through naming
images = os.listdir(added_file_path)
image_names = datas['书名/刊名'].tolist()
image_IDs = datas['序号'].tolist()
for name in image_names:
    for image in images:
        if name in image:
            shutil.copy(os.path.join(added_file_path, image), os.path.join('F:\Download\BLSBookDetailStyle\FormatedImages\cover', 'cover_' + image_IDs[image_names.index(name)] + '.png'))
            # store the new line in the csv file
            with open(destination_csv, 'a', encoding='utf-8') as f:
                f.write(str(mapping_index) + ',' + image_IDs[image_names.index(name)] + ',' + name + ',' + 'None' + ',' + 'None' + '\n')
                mapping_index += 1