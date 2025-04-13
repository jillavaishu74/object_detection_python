import cv2
import time
from datetime import datetime




rtsp_url = 0

output_dir = "output_images/"


import os
os.makedirs(output_dir, exist_ok=True)


# cap = cv2.VideoCapture(rtsp_url)

# if not cap.isOpened():
#     print("Error: Could not open RTSP stream.")
#     exit()


def save_image_from_rtsp():
    last_save_time = time.time()
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("Error: Could not open RTSP stream.")
        exit()
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to read frame.")
                continue

            
            current_time = time.time()

            
            if current_time - last_save_time >= 3:
            # time.sleep(2)
                
                filename = datetime.now().strftime("%Y%m%d%H%M%S.jpg")

            
                cv2.imwrite(os.path.join(output_dir, filename), frame)

                print(f"Saved {filename}")

            
                last_save_time = current_time
                return filename
    except KeyboardInterrupt:
        print("Interrupted by user")


    cap.release()
    cv2.destroyAllWindows()
