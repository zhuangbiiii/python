import cv2
import os
import pandas as pd
import shutil

pd.set_option('future.no_silent_downcasting', True)

# Get all videos in the folder
excel_path = "F:\Download\BLSBookDetailStyle\大屏展示数据_video.xlsx"
df = pd.read_excel(excel_path, dtype=str)
# Remove line break symbols from the value
df = df.replace(r'\n', '', regex=True)
# Replace half width symbols from values to prevent accidental line breaks in CSV files
df = df.replace(r' ', '，', regex=True)
index = 0
video_IDs = df['ID'].to_list()
video_names = df['NAME'].to_list()
type = 'video'
author = df['AUTHOR'].to_list()
press = ''
video_description = df['DESCRIPTION'].to_list()
video_cover_time = df['COVERTIME'].to_list()

# Get videos
video_path = "F:\Download\BLSBookDetailStyle\Videos\Videos"
videos = os.listdir(video_path)
videos = [video for video in videos if video.endswith('.mp4')]

# Cover path to save
cover_path = "F:\Download\BLSBookDetailStyle\Videos\cover"

# Video path to save
video_path_to_save = "F:\Download\BLSBookDetailStyle\Videos\\video"

# Mapping csv file path
# row name = INDEX,ID,TYPE,NAME,AUTHOR,PRESS,DESCRIPTION
mapping_csv = "F:\Download\BLSBookDetailStyle\mappingvideo.csv"

# Get the cover of the video
# match the video name with video
debug = False
for name in video_names:
    index = video_names.index(name)
    for video in videos:
        if name in video:
            videos.remove(video)
            video_to_capture = os.path.join(video_path, video)
            vc = cv2.VideoCapture(video_to_capture)
            fps = int(vc.get(cv2.CAP_PROP_FPS))

            # Get the frame count
            frame_capture = int(video_cover_time[index]) * vc.get(cv2.CAP_PROP_FPS)
            # try get frame
            vc.set(cv2.CAP_PROP_POS_FRAMES, frame_capture)
            ret, frame = vc.read()
            if debug:
                # show the frame
                cv2.imshow('frame', frame)
                # wait input, if Y do nothing, if N print the name
                key = cv2.waitKey(0)
                if key == ord('a'):
                    print(name)
                cv2.destroyAllWindows()
            else:
            # save the frame
                #cv2.imwrite(os.path.join(cover_path, 'cover_' +
                 #       video_IDs[index] + '.png'), frame)
            # copy the video to the video folder
            # and rename it to the video id
               # shutil.copy(video_to_capture, os.path.join(
                #    video_path_to_save, 'video_' + video_IDs[index] + '.mp4'))
                vc.release()
            # Write to csv
            with open(mapping_csv, 'a', encoding='utf-8') as f:
                f.write(f"{index},{video_IDs[index]},{type},{name},{author[index]},{press},{video_description[index]}\n")


            # print(frame_capture)

#print(videos)