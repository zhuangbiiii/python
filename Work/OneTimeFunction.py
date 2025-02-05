import os
import re

stage = 9

if stage == 1:
    # Match all files in a directory without folder

    workspace = 'F:\\Download\\BLSBookDetailStyle\\FormatedImages\\qrcode'
    workspace2 = 'F:\\Download\\BLSBookDetailStyle\\FormatedImages\\cover'

    # Extract IDs from workspace
    qrcode_ids = set()
    for qrcode in os.listdir(workspace):
        match = re.search(r'_(.*?)\.', qrcode)
        if match:
            qrcode_ids.add(match.group(1))

    # Find unmatched files in workspace2
    for cover in os.listdir(workspace2):
        match = re.search(r'_(.*?)\.', cover)
        if match:
            id = match.group(1)
            if id not in qrcode_ids:
                print(f"Unmatched cover file: {cover}")

elif stage == 2:
    import xlwings as xw
    excel = "F:\Download\BLSBookDetailStyle\spacetest.xlsx"
    wb = xw.Book(excel)
    ws = wb.sheets[0]

    arow = ws.range('A1').expand('down').value
    print(arow)
    ## With this test func,we know that the expand('down') will not include the empty cell

elif stage == 3:
    ## Try pandas
    import pandas as pd
    import numpy as np

    # read excel
    excel = "F:\Download\BLSBookDetailStyle\spacetest.xlsx"
    # get a1
    df = pd.read_excel(excel)
    print(df.iloc[0, 0])

    # df = pd.read_excel(excel)
    # column_values = df['id'].tolist()
    # print(column_values)

    ## try write to excel
    # df = pd.DataFrame({'test number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    # writer = pd.ExcelWriter(excel)
    # df.to_excel(writer, sheet_name='Sheet2', index=False)
    # writer._save()
    # writer.close()



    ## The read_excel will not include the empty cell, so we can use the df to get the data we want


elif stage == 4:
    ## Transform the images in the folder to the same format
    import cv2
    import numpy as np
    import os

    workspace = "F:\\Download\\BLSBookDetailStyle\\Images"

    ## All images in the folder will be transformed to the png format to inport to unreal engine
    for file in os.listdir(workspace):
        if file.endswith('.png'):
            continue
        img = cv2.imread(os.path.join(workspace, file))
        
        # cv2.imwrite(os.path.join(workspace, file), img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
        # print(f"Transformed {file} to png successfully!")

elif stage == 5:
    import pandas as pd
    excel = "F:\Download\BLSBookDetailStyle\spacetest.xlsx"
    df = pd.read_excel(excel)
    print(str(df['Text'][4]))

elif stage == 6:
    import pandas as pd
    ## cover ande qrcode check from ecxel
    excel = "F:\Download\BLSBookDetailStyle\大屏展示数据_audio.xlsx"

    cover_path = "F:\Download\BLSBookDetailStyle\首都图书馆\封面"
    qrcode_path = "F:\Download\BLSBookDetailStyle\首都图书馆\二维码"

    ## Read the excel
    df = pd.read_excel(excel,dtype=str)
    cover_files = os.listdir(cover_path)
    qrcode_files = os.listdir(qrcode_path)

    ## book name
    book_names = df['书名/刊名']

    # ## check the cover and qrcode with the book name
    error_index = []
    index = 0
    for book_name in book_names:
        cover_match = False
        qrcode_match = False
        for cover in cover_files:
            if book_name in cover:
                cover_match = True
                break
        for qrcode in qrcode_files:
            if book_name in qrcode:
                qrcode_match = True
                break
        if not cover_match:
            error_index.append(index)
            print(f"Cover not found for {book_name}")
        if not qrcode_match:
            error_index.append(index)
            print(f"Qrcode not found for {book_name}")

        print(f"Check {index} book")
        index += 1

    print(f"Error index: {error_index}")


elif stage == 7:
    # Add extra '_二维码' to the ‘.png' file
    cover_path = "F:\Download\BLSBookDetailStyle\首都图书馆\二维码"
    for file in os.listdir(cover_path):
        if file.endswith('.png'):
            os.rename(os.path.join(cover_path, file), os.path.join(cover_path, file.replace('.png', '_二维码.png')))
            print(f"Add '_二维码' to {file}")

elif stage == 8:
    # Get the specific frame in video
    import cv2
    import os
    import pandas as pd
    import shutil

    # Video path
    video = "F:\Download\BLSBookDetailStyle\Videos\\video\\video_v_18.mp4"
    cover_path = "F:\Download\BLSBookDetailStyle\Videos\cover"
    cover_name = "cover_v_18.png"

    # Get the frame
    vc = cv2.VideoCapture(video)
    vc.set(cv2.CAP_PROP_POS_FRAMES, 2270)
    ret, frame = vc.read()
    # show the frame
    cv2.imshow('frame', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # save the frame
    cv2.imwrite(os.path.join(cover_path, cover_name), frame)

elif stage == 9:
    ## Video check
    video_names_path = "F:\Download\BLSBookDetailStyle\大屏展示数据_video.xlsx"
    import pandas as pd
    df = pd.read_excel(video_names_path, dtype=str)
    video_names = df['NAME']

    videos_path = "F:\Download\BLSBookDetailStyle\Videos\Videos"
    import os
    videos = os.listdir(videos_path)
    for video in videos:
        print(video)
        break
        for name in video_names:
            if name in video:
                break
            