import cv2

# Replace 'rtsp://username:password@your_rtsp_url' with your actual RTSP URL, username, and password
rtsp_url = 'rtsp://test54:123456@192.168.1.231/stream1:554'

# Open the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

while True:
    # Read a frame from the RTSP stream
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('RTSP Stream', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
