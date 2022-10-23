import numpy as np
import helper_video
import os
import cv2
from pathlib import Path


def difference_to_class(image_file_1, image_file_2, threshold=20000000):
    image_1 = helper_video.custom_read_image(image_file_1)
    image_2 = helper_video.custom_read_image(image_file_2)
    diff_image = helper_video.image_difference(image_1, image_2)

    # mark images as interesting depending on absolute difference
    diff = np.sum(diff_image)
    if diff > threshold:
        pth1 = Path(image_file_1)
        base1 = pth1.stem
        folder1 = pth1.parent

        pth2 = Path(image_file_2)
        base2 = pth2.stem
        folder2 = pth2.parent

        print("Interesting difference:", base1, base2)
        try:
            # creating a folder named data
            folder = os.path.join(pth1.parent, "detection")
            print(folder)
            if not os.path.exists(folder):
                os.makedirs(folder)

        # if not created then raise error
        except OSError:
            print('Error: Creating directory of data')
        diff_image_file_name = os.path.join(folder, base1 + "_" + base2 + ".jpg")
        print(diff_image_file_name)
        cv2.imwrite(diff_image_file_name, diff_image)
