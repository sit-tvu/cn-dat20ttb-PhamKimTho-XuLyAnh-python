import numpy as np 
import cv2 
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [6,8]
img = cv2.imread("sanbay.tif", 0)
# Chỉnh kích thước ảnh
def rescale(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv2.resize (frame,(width,height),interpolation=cv2.INTER_AREA)


#using numpy
h2 = np.histogram(img.ravel(), bins=256, range=[0,256])
print(h2[0].shape)
cv2.imshow('Ảnh gốc', img)
plt.plot(h2[0])
plt.show()