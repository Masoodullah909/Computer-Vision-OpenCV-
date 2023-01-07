# Save the Gray and Black video 

import cv2 as cv

cap = cv.VideoCapture('resources/video.mp4')

# Writing format, codec, video object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("resources/Gray_video.avi", cv.VideoWriter_fourcc('M', 'j', 'p', 'G'), 10, (frame_width, frame_height))


while (True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)
    # To show in Player
    if ret == True:
        out.write(grayframe)
        cv.imshow('Video', grayframe)
        # To quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows() 
