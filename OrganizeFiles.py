import re
import os
import shutil
import pandas as pd

debug = True
b_cover = True
b_qrcode = False
pd.set_option('future.no_silent_downcasting', True)

##  Read excel file and get the book name and id
##  and find the corresponding book cover and qrcode
##  then move them to the corresponding folder
##  and rename them to the book id in the excel file

# Destination mapping csv file
destination_csv = "F:\Download\BLSBookDetailStyle\mappingbook.csv"

# Read excel file 
origin_excel = "F:\Download\首图大屏展示数据.xlsx"
book_datas = pd.read_excel(origin_excel, usecols=[0,1,2,3,4], dtype=str) ## Read the first 5 columns to string

# Remove line break symbols from the value
book_datas = book_datas.replace(r'\n', '', regex=True)
# Replace half width symbols from values to prevent accidental line breaks in CSV files
book_datas = book_datas.replace(r' ', '，', regex=True)

# Get book name and id
book_names = book_datas['书名/刊名'].tolist()
book_ids = book_datas['序号'].tolist()

# Get book cover and qrcode
workspace = "F:\Download\BLSBookDetailStyle\Images"
workspace2 = "F:\Download\BLSBookDetailStyle\FormatedImages"

book_cover:list[str] = []
book_qrcode:list[str] = []

images = os.listdir(workspace)
# split the images into cover and qrcode
for image in images:
    match = re.search(r'_二维码(.*?)\.', image)
    if match:
        book_qrcode.append(image)
    else:
        book_cover.append(image)
#print(book_cover)
print(book_qrcode)

# Initialize the mapping csv file 
with open(destination_csv, 'w', encoding='utf-8') as f:
    f.write("INDEX,ID,TYPE,NAME,AUTHOR,PRESS,DESCRIPTION\n")

# If find the corresponding book cover and qrcode
# copy them to the corresponding folder
# and rename them to the book id in the excel file
type = 'book'
for i, name in enumerate(book_names):
    for covrt in book_cover:
        name_match = re.search(name, covrt)
        # If find the corresponding book cover
        if name_match:
            for qrcode in book_qrcode:
                qrcode_match = re.search(name, qrcode)
                # If find the corresponding book qrcode
                if qrcode_match:

                    if debug:
                        print(os.path.join(workspace, covrt))
                        print(os.path.join(workspace, qrcode))
                        print(os.path.join(workspace2, 'cover', 'cover_' + book_ids[i] + '.png'))
                        print(os.path.join(workspace2, 'qrcode', 'qrcode_' + book_ids[i] + '.png') + '\n')

                    # copy the book cover and qrcode to the corresponding folder
                    shutil.copy(os.path.join(workspace, covrt), os.path.join(workspace2, 'cover', 'cover_' + book_ids[i] + '.png'))
                    shutil.copy(os.path.join(workspace, qrcode), os.path.join(workspace2, 'qrcode', 'qrcode_' + book_ids[i] + '.png'))

                    # Overwrite the found row book's index(=ID), ID, NAME, AUTHOR, PRESS, DESCRIPTION to the mapping csv file
                    # NOTE: In UTF-8, the csv file will be encoded in UTF-8-BOM, which is not supported by Unreal Engine
                    #       So we need to convert the csv file to UTF-8 without BOM

                    with open(destination_csv, 'a', encoding='utf-8') as f:
                        f.write(f"{i},{book_ids[i]},{type},{name},{book_datas['作者'][i]},{book_datas['出版社'][i]},{book_datas['简介'][i]}\n")

                    book_cover.remove(covrt)
                    book_qrcode.remove(qrcode)

                    # print(f"Move {covrt} and {qrcode} to {book_ids[i]}.png")
                    break
            break



#print(covrt)