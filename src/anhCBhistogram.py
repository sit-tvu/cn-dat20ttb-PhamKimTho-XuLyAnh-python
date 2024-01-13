import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh từ đường dẫn
img_org = cv2.imread('sanbay.tif')
# Chỉnh kích thước ảnh
def rescale(frame, scale=0.7):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv2.resize (frame,(width,height),interpolation=cv2.INTER_AREA)
img = rescale(img_org)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# hàm xử lý cân bằng histogram
img_equalize = cv2.equalizeHist(img_gray)
cv2.imshow('anh cb Histogram', img_equalize)
hist_equalize = cv2.calcHist([img_equalize],[0],None,[256],[0,256])


plot1 = plt.figure(2)
plt.title('Histogram Anh sau CB')
plt.plot(hist_equalize)

plt.show()
