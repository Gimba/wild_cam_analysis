import cv2
import os


def extract_image_from_video(video_file, interval):
    video_data = cv2.VideoCapture(video_file)

    try:
        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')
