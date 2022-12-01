# pip install pillow

from PIL import Image
import os
import time
                # ↓ 替换成你想转换的GIF的和本脚本的相对位置
gifFileName = '5.gif'
gif = Image.open(gifFileName)
pngDir = str(time.time())
#新建文件夹.jpg
os.mkdir(pngDir)

def __main__(show,tile):
    if(tile):
        __funcb__(show)
    else:
        __funca__()

# round是四舍五入不满足我们需要的条件，自己写一个
def __round__(a):
    if(a%10 > 0):
        if(a%10 > 5):
            return round(a/10)
        else:
            return round(a/10+1)
    else:
        return round(a/10)

# 单独存放每一帧
def __funca__():
    try:
        while True:
            #保存当前帧图片
            current = gif.tell()
            gif.save(pngDir+'/'+str(current)+'.png')
            #获得下一帧
            gif.seek(current+1)
    except EOFError:
        pass

# 组合成一张png
def __funcb__(bool):
    #png瓦片大小
    size = [gif.size[0]*10,gif.size[1]*(__round__(gif.n_frames))]
    #png瓦片容器
    im = Image.new('RGBA',size)
    counter = 0
    for i in range(__round__(gif.n_frames)):
        for j in range(10):
            if(counter < gif.n_frames):
                print(str(counter)+'/'+str(gif.n_frames))
                gif.seek(counter)
                im.paste(gif,(gif.size[0]*j,gif.size[1]*i))
                counter+=1
                    
    im.save(pngDir+'/giftopng'+str(gif.size)+'.png')
    if(bool):
        im.show()

__main__(True,False)