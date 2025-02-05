import pandas as pd
import os

## Append which video has dexcription

# Source excel file
source_excel = "F:\Download\BLSBookDetailStyle\Videos\电子书大屏-资源清单.xlsx"
source_excel2 = "F:\Download\BLSBookDetailStyle\Videos\\20241225-首图动漫在线系列简介.xlsx"

# Video folder
video_folder = "F:\Download\BLSBookDetailStyle\Videos\Videos"

# Destination excel file
destination_excel = "F:\Download\BLSBookDetailStyle\大屏展示数据_video.xlsx"

# Read the source excel file
df = pd.read_excel(source_excel)
df2 = pd.read_excel(source_excel2)

video_names = df['资源名称']
video_names2 = df2['系列名称']

# Find the video with names
videos = os.listdir(video_folder)
for video_name in video_names:
    for video in videos:
        if video_name in video:
            print(video_name)
            break

#print(videos_name)