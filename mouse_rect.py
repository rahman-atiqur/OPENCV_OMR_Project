# # import required libraries
# import cv2
# import numpy as np
# drawing = False
# ix,iy = -1,-1

# # define mouse callback function to draw circle
# def draw_rectangle(event, x, y, flags, param):
#    global ix, iy, drawing, img
#    if event == cv2.EVENT_LBUTTONDOWN:
#       drawing = True
#       ix = x
#       iy = y
#    elif event == cv2.EVENT_MOUSEMOVE:
#       if drawing == True:
#          cv2.rectangle(img, (ix, iy), (x, y),(0, 0, 255),-1)
#       elif event == cv2.EVENT_LBUTTONUP:
#          drawing = False
#          cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)

# # Create a black image
# img = np.zeros((512,700,3), np.uint8)

# # Create a window and bind the function to window
# cv2.namedWindow("Rectangle Window")

# # Connect the mouse button to our callback function
# cv2.setMouseCallback("Rectangle Window", draw_rectangle)

# # display the window
# while True:
#    cv2.imshow("Rectangle Window", img)
#    if cv2.waitKey(10) == 27:
#       break
# cv2.destroyAllWindows()

#########################################
# import numpy as np
# import cv2
# # import cv2.cv as cv

# boxes = []

# def on_mouse(event, x, y, flags, params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#          print ('Start Mouse Position: '+str(x)+', '+str(y))
#          sbox = [x, y]
#          boxes.append(sbox)

#     elif event == cv2.EVENT_LBUTTONUP:
#         print ('End Mouse Position: '+str(x)+', '+str(y))
#         ebox = [x, y]
#         boxes.append(ebox)


# count = 0
# while(1):
#     count += 1
#     img = cv2.imread('img.jpg',0)
#     img = cv2.blur(img, (3,3))

#     cv2.namedWindow('real image')
#     cv2.SetMouseCallback('real image', on_mouse, 0)
#     # cv2.setMouseCallback("image",printCoordinate)
#     cv2.imshow('real image', img)
#     if count < 50:
#         if cv2.waitKey(33) == 27:
#             cv2.destroyAllWindows()
#             break
#     elif count >= 50:
#         if cv2.waitKey(0) == 27:
#             cv2.destroyAllWindows()
#             break
#         count = 0
######################################
# import required libraries
# import cv2
# import numpy as np
# drawing = False
# ix,iy = -1,-1

# # define mouse callback function to draw circle
# def draw_rectangle(event, x, y, flags, param):
#    global ix, iy, drawing, img
#    if event == cv2.EVENT_LBUTTONDOWN:
#       drawing = True
#       ix = x
#       iy = y
#    elif event == cv2.EVENT_MOUSEMOVE:
#       if drawing == True:
#          cv2.rectangle(img, (ix, iy), (x, y),(0, 0, 255),-1)
#       elif event == cv2.EVENT_LBUTTONUP:
#          drawing = False
#          cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)

# # Create a black image
# img = np.zeros((512,700,3), np.uint8)

# # Create a window and bind the function to window
# cv2.namedWindow("Rectangle Window")

# # Connect the mouse button to our callback function
# cv2.setMouseCallback("Rectangle Window", draw_rectangle)

# # display the window
# while True:
#    cv2.imshow("Rectangle Window", img)
#    if cv2.waitKey(10) == 27:
#       break
# cv2.destroyAllWindows()



#######################################
import cv2

image = cv2.imread('OMR_100.jpg')
height, width, channels = image.shape
start_point = (0,0)
end_point = (width, height)
color = (0,0,255)
thickness = 5

image = cv2.rectangle(image, start_point, end_point, color, thickness)
# img=cv2.imread('OMR_100.jpg')
# img=cv2.resize(img,(1241,1754))
# cv2.imshow("image",img)
cv2.imshow('Rectangle',image)
cv2.waitKey()