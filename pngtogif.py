# pip install pillow

from PIL import Image
import os
            # ↓ 放进这个文件夹，命好名，0~n.png
imDir = '1669885351.5980227/'

def __createGif__():
    frames = []
    a = len(os.listdir(imDir))
    for b in range(a):
        print(b)
        frames.append(Image.open(imDir+str(b)+'.png'))

    frames[0].save('new.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)

__createGif__()
