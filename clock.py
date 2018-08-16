#!/usr/bin/env python3

"""
sudo apt-get install python3 python3-dev python3-pip git python3-rpi.gpio python3-smbus python3-PIL
pip3 install unicornhadhd
"""

import datetime
from PIL import Image, ImageDraw, ImageFont
import unicornhathd
import time

COLOR = (200, 0, 0)

width, height = unicornhathd.get_shape()

unicornhathd.rotation(0)
unicornhathd.brightness(0.5)

font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 8)

while True:
    image = Image.new("RGB", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    now = datetime.datetime.now()
    draw.text((0, 0), '{0:02}'.format(now.hour), fill=COLOR, font=font)
    draw.text((0, 8), '{0:02}'.format(now.minute), fill=COLOR, font=font)

    unicornhathd.clear()
    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            unicornhathd.set_pixel(width-x-1, y, r, g, b)

    if now.second % 2:
        unicornhathd.set_pixel(0, height-1, *COLOR)
        unicornhathd.set_pixel(1, height-1, *COLOR)
        unicornhathd.set_pixel(0, height-2, *COLOR)
        unicornhathd.set_pixel(1, height-2, *COLOR)
    unicornhathd.show()

    time.sleep(0.1)
