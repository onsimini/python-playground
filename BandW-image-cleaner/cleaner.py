import cv2

filename = r'org.jpg'
img = cv2.imread(filename)

for y in range(len(img)):
    for x in range(len(img[y])):
        if img[y, x, 1] < 128:
            img[y, x] = [0, 0, 0]
        else:
            img[y, x] = [255, 255, 255]

cv2.imwrite('cleaned.jpg', img)
