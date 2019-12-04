#!/usr/bin/python

import os
import sys
import numpy as np
import cv2
from skein import skein1024, skein512, skein256


def image_hash(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        return None

    else:
        image_string = image.tostring()
        hashed = skein1024(image_string, digest_bits=384)

        return hashed.hexdigest()


def main():
    for line in sys.stdin:
        file_name = line.strip()
        hased_string = image_hash(file_name)

        if hased_string is not None:
            print ("%s\t%s" % (hased_string, file_name))


if __name__ == "__main__":
    main()