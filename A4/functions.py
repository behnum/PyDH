# Behnam Baharmand

import glob
from PIL import Image

# Function Defenitions @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
images_list = glob.glob("./A4/img/*.jpg") + glob.glob("./A4/img/*.png")


def calc_mean(images_list=None, channel="r"):
    """
    Goes through each pixel of any given channel and calculates the mean.

    Parameters:
    images_list(list): List of image files
    channel(str): R, G, or B as in RGB additive color model

    Returns:
    list: The sorted list of findings as detailed in the task requirements

    """
    if images_list == None or type(images_list) != list:  # (Rudimentary) error proofing
        return -1

    output_list = []
    for item in images_list:
        img = Image.open(item)
        pixel_values = []

        for row in range(0, img.size[1]):
            for column in range(0, img.size[0]):
                r, g, b, *_ = img.getpixel((column, row))
                # using __dunder__ methods for brevity (refer to report for more)
                if channel == "r":
                    pixel_values += [r]
                elif channel == "g":
                    pixel_values += [g]
                else:
                    pixel_values += [b]

        output_list.append([sum(pixel_values) // len(pixel_values), img])

    sorted_list = sorted(output_list, key=lambda x: x[0])
    return sorted_list


def nonuple_collage_builder(images_list=images_list, img_width=640, img_height=480):
    """
    Generate and save a collage based on the given image list.

    Parameters:
    images_list(list): List of image files
    img_width(int): Width of each image in pixels, default is 640px
    img_height(int): Height of each image in pixels, default is 480px

    """
    total_width = img_width * 3
    total_height = img_height * 3

    new_img = Image.new("RGB", (total_width, total_height))

    x, y = 0, 0

    for img in images_list:
        if x == total_width:
            y = y + img_height
            x = 0
        img = Image.open(img)
        new_img.paste(img, (x, y))
        x = x + img_width

    new_img.save("./A4/collage.png")
