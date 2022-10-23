import cv2
import os
from pathlib import Path


def extract_image_from_video(video_file, frame_interval=100):
    pth = Path(video_file)
    video_data = cv2.VideoCapture(video_file)

    try:
        # creating a folder named data
        folder = os.path.join(pth.parent, pth.stem)
        if not os.path.exists(folder):
            os.makedirs(folder)

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    # frame counter
    current_frame = -1

    while (True):
        current_frame += 1
        # reading from frame
        ret, frame = video_data.read()
        print(current_frame % frame_interval)
        if ret:
            if current_frame % frame_interval == 0:
                # if video is still left continue creating images
                name = os.path.join(folder, 'frame_' + str(current_frame) + '.jpg')
                print('Creating...' + name)

                # writing the extracted images
                cv2.imwrite(name, frame)

                # increasing counter so that it will
                # show how many frames are created

        else:
            break

    # Release all space and windows once done
    video_data.release()
    cv2.destroyAllWindows()

def image_difference(image_file_1, image_file_2):
    img_1 = cv2.imread(image_file_1)
    img_2 = cv2.imread(image_file_2)
    image3 = cv2.absdiff(img_1, img_2)
    # cv2.imwrite("diff.jpg", image3)
    return image3