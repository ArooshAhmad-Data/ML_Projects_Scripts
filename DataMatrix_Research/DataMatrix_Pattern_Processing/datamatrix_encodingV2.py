# -*- coding: utf-8 -*-
"""
Created on Tue May 10 22:25:56 2022

@author: richa
"""

#https://pypi.org/project/pylibdmtx/
from PIL import Image


from pylibdmtx.pylibdmtx import encode
from pylibdmtx.pylibdmtx import decode
import numpy as np
#import ppf.datamatrix
#encoded = encode('hello world'.encode('utf8'))
#encoded = encode('Digitho'.encode('utf_8'))

encoded = encode('DIGITHO/00000000'.encode('utf_8'))


#encoded = encode('                '.encode('utf_8'))
img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels )
img.save('dmtx.png')
print(decode(Image.open('dmtx.png')))
print('encoded.width', encoded.width)
print('encoded.height', encoded.height)
#[Decoded(data=b'hello world', rect=Rect(left=9, top=10, width=80, height=79))]
#print('encoded= ', encoded)
pixels = list(img.getdata())
#print('pixels= ', pixels)



################### Create image from SVG 
encoded_str = str(encoded)
x1 = encoded_str.index("pixels=b'")
print('x',x1)
print('len= ', len(encoded_str), ';',encoded_str[len(encoded_str)-1:len(encoded_str)])
print('12',encoded_str[x1+9:x1+13])
makelist = []
imagematrix = []
code_array = []
XY_matrix = np.zeros((20,20))



counter = x1+13
y = 0
x = 1
#for x in range(x1+13, len(encoded_str)-2, 60):
while counter < len(encoded_str)-2:
    for x in range(20):
        makelist.append(encoded_str[counter:counter+12])
        counter = counter + 60
    y = y + 1
    counter = counter + 1200*4
    #print('y',y)

#makelist.append(encoded_str[counter:x+4]) #Add last string


#print('makelist',makelist)
print('makelist len',len(makelist))
#print('makelist',makelist[2])

########Create a matrix
x = 0
y = 0
for p in range(0,len(makelist)):
    if makelist[p] == makelist[0]: # == '\xff'
        code_array = code_array + [(255,255,255)]* 1
        
    else:
        code_array = code_array + [(0,0,0)]*1
        coor = int(x),int(y)
        XY_matrix[int(x) , int(y)] = 1
        print('x',x,'y',y)
        print('p',p)
    x = x + 1
    if x > 19:
        x= 0
        y = y + 1

#print('code_array', code_array)
#print('--',encoded_str[50:54],'--')
#if encoded_str[50:54] == makelist[0]:
#    print('yeah')
print('XY_matrix=',XY_matrix)
XY_matrix= XY_matrix.transpose()
print('XY_matrix=',XY_matrix)

list_of_pixels = list(code_array)
#im = Image.new('RGB', (encoded.width , encoded.height))
im = Image.new('RGB', (20 , 20))
im.putdata(list_of_pixels)
im.show()
#image_icon.save('image_icon82.png', format = 'PNG')
im.save('datamatrix.png', format = 'PNG')
print(im.format, im.size, im.mode)



############################################
###Decoding

import numpy as np
import cv2
from pylibdmtx import pylibdmtx

if __name__ == '__main__':

    image = cv2.imread('dmtx.png', cv2.IMREAD_UNCHANGED);

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret,thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    msg = pylibdmtx.decode(thresh)
    print('message is:', msg)

"""
encode format:
'ascii',
 'big5',
 'big5hkscs',
 'cp037',
 'cp273',
 'cp424',
 'cp437',
 'cp500',
 'cp720',
 'cp737',
 'cp775',
 'cp850',
 'cp852',
 'cp855',
 'cp856',
 'cp857',
 'cp858',
 'cp860',
 'cp861',
 'cp862',
 'cp863',
 'cp864',
 'cp865',
 'cp866',
 'cp869',
 'cp874',
 'cp875',
 'cp932',
 'cp949',
 'cp950',
 'cp1006',
 'cp1026',
 'cp1125',
 'cp1140',
 'cp1250',
 'cp1251',
 'cp1252',
 'cp1253',
 'cp1254',
 'cp1255',
 'cp1256',
 'cp1257',
 'cp1258',
 'cp65001',
 'euc_jp',
 'euc_jis_2004',
 'euc_jisx0213',
 'euc_kr',
 'gb2312',
 'gbk',
 'gb18030',
 'hz',
 'iso2022_jp',
 'iso2022_jp_1',
 'iso2022_jp_2',
 'iso2022_jp_2004',
 'iso2022_jp_3',
 'iso2022_jp_ext',
 'iso2022_kr',
 'latin_1',
 'iso8859_2',
 'iso8859_3',
 'iso8859_4',
 'iso8859_5',
 'iso8859_6',
 'iso8859_7',
 'iso8859_8',
 'iso8859_9',
 'iso8859_10',
 'iso8859_11',
 'iso8859_13',
 'iso8859_14',
 'iso8859_15',
 'iso8859_16',
 'johab',
 'koi8_r',
 'koi8_t',
 'koi8_u',
 'kz1048',
 'mac_cyrillic',
 'mac_greek',
 'mac_iceland',
 'mac_latin2',
 'mac_roman',
 'mac_turkish',
 'ptcp154',
 'shift_jis',
 'shift_jis_2004',
 'shift_jisx0213',
 'utf_32',
 'utf_32_be',
 'utf_32_le',
 'utf_16',
 'utf_16_be',
 'utf_16_le',
 'utf_7',
 'utf_8',
 'utf_8_sig'
 """