import cv2

device_id = 1
cap = cv2.VideoCapture(device_id)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'H264')
writer = cv2.VideoWriter('./output/video.avi', fourcc, 30, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break 

    writer.write(frame)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

writer.release()
cap.release()
cv2.destroyAllWindows()
