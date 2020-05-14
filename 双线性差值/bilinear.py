# -*- coding: utf-8 -*-
# Author: lmh
# Time: 2018.10.22
from skimage import transform
import matplotlib.pyplot as plt
import matplotlib.image as mping
import numpy as np


def chazhi(x, y, im):
    # x,y分别是缩放或者放大后对应源图像的浮点坐标位置，im是源图像，返回目标图像根据插值计算得到的像素值
    x1, y1 = int(x), int(y)  # x1,x2,x3,x4分别是插值坐标对应在源图像上下左右最近的点的坐标
    x2, y2 = x1 + 1, y1 + 1
    pixel11, pixel21, pixel12, pixel22 = im[x1 - 1, y1 - 1], im[x2 - 1, y1 - 1], im[x2 - 1, y1 - 1], im[x2 - 1, y2 - 1]
    # 以下是根据双线性插值的公式求得的目标图像的该位置的像素值
    new_pixel = (x2 - x) * (y2 - y) * pixel11 + (x - x1) * (y2 - y) * pixel21 + (x2 - x) * (y - y1) * pixel12 + (x - x1) * (
                y - y1) * pixel22
    return new_pixel

im = mping.imread('C:\\Users\\shou\\Desktop\\photo.png')
im11 = im
scale = 0.4  # 缩小程度
row, col = int(im.shape[0] * scale), int(im.shape[1] * scale)
im_sml = np.zeros([row, col, 3])
for k in range(3):
    im1 = im[:, :, k]
    for i in range(row):
        for j in range(col):
            value = chazhi(i / scale, j / scale, im1)  # 3通道图像逐像素计算缩小或者放大后的新像素值
            im_sml[i][j][k] = value

im_narrow = im_sml

scale = 1.7  # 扩大程度
row, col = int(im.shape[0] * scale), int(im.shape[1] * scale)
im_sml = np.zeros([row, col, 3])
for k in range(3):
    im1 = im[:, :, k]
    for i in range(row):
        for j in range(col):
            value = chazhi(i / scale, j / scale, im1)
            im_sml[i][j][k] = value

im_enlarge = im_sml
python_narrow = transform.resize(im, (175, 145))  # 使用skimage自带函数resize图像，也可以直接写像上面一样写比例（0.4,1.7）
python_enlarge = transform.resize(im, (746, 617))  # 为了对比，两种方法特意放大和缩小一样大小

plt.figure()
plt.subplot(151)
plt.imshow(im11, plt.cm.gray)
plt.title('Original')
# plt.axis('off')

plt.subplot(152)
plt.imshow(im_narrow, plt.cm.gray)
plt.title('my_narrow')
# plt.axis('off')

plt.subplot(153)
plt.imshow(python_narrow, plt.cm.gray)
plt.title('skimage_narrow')
# plt.axis('off')

plt.subplot(154)
plt.imshow(im_enlarge, plt.cm.gray)
plt.title('my_enlarge')
# plt.axis('off')

plt.subplot(1, 5, 5)
plt.imshow(python_enlarge, plt.cm.gray)
plt.title('skimage_enlarge')
# plt.axis('off')
plt.savefig('image_comp.png')