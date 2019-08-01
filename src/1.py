import cv2

# BGR
img = cv2.imread("imori.jpg")
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# RGB
img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

cv2.imwrite("imori_out.jpg", img)
cv2.imshow("imori", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

