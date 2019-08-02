import cv2
import numpy as np
import matplotlib.pyplot as plt

# BGR
img = cv2.imread("imori.jpg")
H, W, _ = img.shape
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# Gray Scale
out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

# find threshold with
f_max = 0
f_maxarg = 0
x = np.arange(0,256,1)
y = np.zeros_like(x)
for _t in range(1, 255):
    v0 = out[np.where(out < _t)]
    m0 = np.mean(v0) if len(v0) > 0 else 0
    w0 = len(v0) / (H * W)
    v1 = out[np.where(out >= _t)]
    m1 = np.mean(v1) if len(v1) > 0 else 0
    w1 = len(v1) / (H * W)
    f = w0 * w1 * (m0-m1)**2
    y [_t] = f
    if(f > f_max):
        f_max = f
        f_maxarg = _t
t = f_maxarg


out[out < t] = 0
out[out >= t] = 255

print(t)
plt.plot(x, y)
plt.show()

# cv2.imwrite("imori_out.jpg", out)
cv2.imshow("imori", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

