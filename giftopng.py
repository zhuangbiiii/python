# pip install pillow

from PIL import Image
import os
import time
                # �� �滻������ת����GIF�ĺͱ��ű������λ��
gifFileName = '5.gif'
gif = Image.open(gifFileName)
pngDir = str(time.time())
#�½��ļ���.jpg
os.mkdir(pngDir)

def __main__(show,tile):
    if(tile):
        __funcb__(show)
    else:
        __funca__()

# round���������벻����������Ҫ���������Լ�дһ��
def __round__(a):
    if(a%10 > 0):
        if(a%10 > 5):
            return round(a/10)
        else:
            return round(a/10+1)
    else:
        return round(a/10)

# �������ÿһ֡
def __funca__():
    try:
        while True:
            #���浱ǰ֡ͼƬ
            current = gif.tell()
            gif.save(pngDir+'/'+str(current)+'.png')
            #�����һ֡
            gif.seek(current+1)
    except EOFError:
        pass

# ��ϳ�һ��png
def __funcb__(bool):
    #png��Ƭ��С
    size = [gif.size[0]*10,gif.size[1]*(__round__(gif.n_frames))]
    #png��Ƭ����
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