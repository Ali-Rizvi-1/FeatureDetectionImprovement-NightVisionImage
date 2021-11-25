import numpy as np
import cv2

img = cv2.imread('LionImage2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

kp = sift.detect(gray,None)
print('Lion Image',kp,'first keypoints', len(kp), 'length of keypoints')

img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#cv2.imwrite('Lion_sift_keypoints.jpg',img)

cv2.imshow("Ïmage", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('LionImageNightVision.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

kp = sift.detect(gray,None)
print('Night Vision Lion Image',kp,'second keypoints', len(kp), 'length of keypoints')

img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#cv2.imwrite('NVLion_sift_keypoints.jpg',img)

cv2.imshow("Ïmage", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('AdjustedLionImage.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

kp = sift.detect(gray,None)
print('Adjusted Night Vision Image',kp,'third keypoints', len(kp), 'length of keypoints')

img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#cv2.imwrite('Adjusted_NVLion_sift_keypoints.jpg',img)

cv2.imshow("Ïmage", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
