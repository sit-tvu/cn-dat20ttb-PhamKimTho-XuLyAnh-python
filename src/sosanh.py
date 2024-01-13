import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [6,4]
# Đọc ảnh từ đường dẫn
img_org = cv2.imread('sanbay.tif')
# Chỉnh kích thước ảnh
def rescale(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv2.resize (frame,(width,height),interpolation=cv2.INTER_AREA)
img = rescale(img_org)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('anh goc', img_gray)
hist = cv2.calcHist([img],[0],None,[256],[0,256])

img_equalize = cv2.equalizeHist(img_gray)
cv2.imshow('anh cb Histogram', img_equalize)
hist_equalize = cv2.calcHist([img_equalize],[0],None,[256],[0,256])

plot1 = plt.figure(1)
plt.title('Histogram Anh goc')
plt.plot(hist)

plot1 = plt.figure(2)
plt.title('Histogram Anh sau CB')
plt.plot(hist_equalize)

plt.show()