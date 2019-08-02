import cv2
import numpy as np

SIZE = 8

# Read image
img = cv2.imread("imori.jpg")
H, W, C = img.shape
h = H//SIZE
w = W//SIZE

img = img[:h*SIZE, :w*SIZE, :].copy()
img = np.reshape(img, (h, SIZE * SIZE, w, C))
img = np.average(img, axis=1).astype(int)
print(img.shape)

out = img

cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()