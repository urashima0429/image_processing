import cv2
import numpy as np

# BGR
img = cv2.imread("imori.jpg")
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# Gray Scale
out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

# cv2.imwrite("imori_out.jpg", out)
cv2.imshow("imori", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

