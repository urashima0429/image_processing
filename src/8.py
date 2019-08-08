import cv2
import numpy as np

SIZE = 4

# Read image
img = cv2.imread("imori.jpg")
H, W, C = img.shape
h = H//SIZE
w = W//SIZE

img = img[:h*SIZE, :w*SIZE, :].copy()
for i in range(h):
    for j in range(w):
        img[i*SIZE:(i+1)*SIZE, j*SIZE:(j+1)*SIZE, :] =\
            np.max(img[i*SIZE:(i+1)*SIZE, j*SIZE:(j+1)*SIZE, :], (0, 1))

cv2.imwrite("out.jpg", img)
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()