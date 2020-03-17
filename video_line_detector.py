import cv2
import numpy as np

def nothing(x):
    pass
video = cv2.VideoCapture("/Users/kaisiuho/Opencv_Learn/vdemo1.mp4")

#cv2.namedWindow("Trackbars")
#cv2.createTrackbar("L-H", "Trackbars", 25, 180, nothing)
#cv2.createTrackbar("L-S", "Trackbars", 19, 255, nothing)
#cv2.createTrackbar("L-V", "Trackbars", 51, 255, nothing)
#cv2.createTrackbar("U-H", "Trackbars", 30, 180, nothing)
#cv2.createTrackbar("U-S", "Trackbars", 30, 255, nothing)
#cv2.createTrackbar("U-V", "Trackbars", 94, 255, nothing)

while True:
    ret, orig_frame = video.read()       #ret tell whether there is frame in the video
    if not ret:                     #loop the video
        video = cv2.VideoCapture("/Users/kaisiuho/Opencv_Learn/vdemo1.mp4")
        continue
    gray = cv2.cvtColor(orig_frame,cv2.COLOR_BGR2GRAY)
    smoothed = cv2.GaussianBlur(gray, (1,1),0)
    edges = cv2.Canny(smoothed,50,150,3)
    #hsv = cv2.cvtColor(smoothed, cv2.COLOR_BGR2HSV)

    #l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    #l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    #l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    #u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    #u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    #u_v = cv2.getTrackbarPos("U-V", "Trackbars")


    #low_white = np.array([l_h,l_s,l_v])
    #high_white = np.array([u_h,u_s,u_v])
    #mask = cv2.inRange(hsv, low_white, high_white)
    #edges = cv2.Canny(mask, 75, 150)


    lines_p = cv2.HoughLinesP(edges, 1, np.pi/180, 50, None,100,5)
    print ("line[1]:", lines_p)
    if lines_p is not None:
        for p1 in lines_p:
            x1, y1, x2, y2 = p1[0]
            cv2.line(orig_frame, (x1,y1), (x2,y2), (255,0,0),3)
    cv2.imshow("HoughLinesP", orig_frame)
    cv2.waitKey(0)
    


    #if lines is not None:
        #for line in lines:
            #x1, y1, x2, y2 = line[0]
            #cv2.line(frame, (x1,y1), (x2,y2), (0,255,0),5)
    

    #cv2.imshow("frame", frame)
    #cv2.imshow("edges",edges)

    key = cv2.waitKey(25)
    if key == 27:
        break
video.release()
cv2.destoryAllWindows()
