import cv2

cap = cv2.VideoCapture(0)

currentFrame = 0
while(True):
    ret, frame = cap.read()
    cv2.imshow('img',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    currentFrame += 1

cap.release()
cv2.destroyAllWindows()