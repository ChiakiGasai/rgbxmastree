from tree import RGBXmasTree
from colorzero import Color, Hue
from time import sleep

tree = RGBXmasTree()

tree.color = Color('red')


"""
try:
    while True:
        #tree.color += Hue(deg=1)
        for pixel in tree:
            pixel.color += Hue(deg=1)
            sleep(1)
except KeyboardInterrupt:
    tree.close()
"""

for pixel in tree:
    pixel.color += Hue(deg=1)
    sleep(1)