import sys

import numpy as np
from PIL import Image, ImageOps

WIDTH = 200
MAP = '."/>!*%$#@'
RANGE_SIZE = 255 // len(MAP)

def generate(image_file, output_width):
    # Grayscale
    img = Image.open(image_file)
    gray_img = ImageOps.grayscale(img)
    arr = np.asarray(gray_img)

    bin_size = gray_img.size[0] // output_width
    new_height = gray_img.size[1] // bin_size

    pooled_img = np.squeeze(
        arr.reshape(
            (1, new_height, bin_size, output_width, bin_size)
        ).max(4).max(2))

    # For debugging pooled output
    # im = Image.fromarray(pooled_img)
    # im.show()

    return pooled_img


def draw(img):
    with open('output.txt', 'w') as f:
        for row in img:
            line = ''.join([MAP[min(val // RANGE_SIZE, 9)] for val in row])
            print(line)
            f.write(line + '\n')


if __name__ == '__main__':
    image_file = "images/doom.jpeg"
    if len(sys.argv) > 1:
        image_file = sys.argv[1]

    width = WIDTH
    if len(sys.argv) > 2:
        width = int(sys.argv[2])

    im = generate(image_file, width)
    draw(im)
