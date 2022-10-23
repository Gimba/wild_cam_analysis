import cv2
import os
from pathlib import Path
import glob


def extract_image_from_video(video_file, frame_interval=100):
    pth = Path(video_file)
    video_data = cv2.VideoCapture(video_file)
    folder = os.path.join(pth.parent, pth.stem)
    create_dir(folder)

    # frame counter
    current_frame = -1

    image_files = []

    while (True):
        current_frame += 1
        # reading from frame
        ret, frame = video_data.read()
        if ret:
            if current_frame % frame_interval == 0:
                # if video is still left continue creating images
                name = os.path.join(folder, 'frame_' + str(current_frame) + '.jpg')
                print('Creating...' + name)

                image_files.append(name)
                # writing the extracted images
                cv2.imwrite(name, frame)

                # increasing counter so that it will
                # show how many frames are created

        else:
            break
    # image_files = [os.path.join(video_file.split(".")[0], f) for f in image_files]
    image_files = sorted(image_files, key=lambda x: int(x.split("_")[1].split(".")[0]))
    # Release all space and windows once done
    video_data.release()
    cv2.destroyAllWindows()
    return image_files


def image_difference(img_1, img_2):
    image3 = cv2.absdiff(img_1, img_2)
    # cv2.imwrite("diff.jpg", image3)
    return image3


def custom_read_image(image_file):
    img = cv2.imread(image_file)
    # removing status bar
    img = img[:1020, :]
    return img


def create_dir(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')
