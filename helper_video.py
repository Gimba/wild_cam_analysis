import cv2
import os
from pathlib import Path

def extract_image_from_video(video_file, frame_interval):
    pth = Path(video_file)
    video_data = cv2.VideoCapture(video_file)

    try:
        # creating a folder named data
        folder = os.path.join(pth.parent,pth.stem)
        if not os.path.exists(folder):
            os.makedirs(folder)

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')
