import cv2
import numpy as np

img=cv2.imread('circuit.png')
img=cv2.resize(img,(500,500))
#for getting consecutive 5 or 6 pyrdown image we use loops
layer=img.copy()
gp=[layer]
for i in range(5): #for gaussian pyramid
    layer=cv2.pyrDown(layer)
    gp.append(layer)
#s0 this was the gaussian pyramid
#now lets try laplacian pyramid
layer=gp[4]
cv2.imshow("upper pyramid",layer)
lp=[layer]

for i in range(4, 0, -1): #so this is the laplacian pyramid it looks like edge detection
    size=(gp[i-1].shape[1],gp[i-1].shape[0])
    gaussian_extension=cv2.pyrUp(gp[i],dstsize=size)
    laplacian=cv2.subtract(gp[i-1],gaussian_extension)
    cv2.imshow(str(i),laplacian)
cv2.imshow("original",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
