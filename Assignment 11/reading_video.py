import cv2

cap = cv2.VideoCapture("images/demo.mp4")

while True:
    ret, frame = cap.read()
    
    if ret == False:
        break
    
    cv2.imshow("Video", frame)
    
    if cv2.waitKey(25) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()