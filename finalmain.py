import cv2

tracker = cv2.TrackerKCF_create()
video = cv2.VideoCapture(0)

while True:
    k,frame = video.read()
    cv2.imshow("Tracking",frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
bbox = cv2.selectROI(frame, False)

ok = tracker.init(frame, bbox)
cv2.destroyWindow("ROI selector")

while True:
    ok, frame = video.read()
    ok, bbox = tracker.update(frame)

    if(ok):
        x, y, w, h = [int(v) for v in bbox]
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]),int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0,0,255), 2, 2)
        cropped_frame = frame[y:y+h, x:x+w]
    cv2.imshow("Tracking", frame)
    cv2.imshow("ROI Tracking",cropped_frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break