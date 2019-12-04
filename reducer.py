#!/usr/bin/python

import sys


def main():
    current_key = None
    current_image = None
    runner_key = None
    runner_image = None
    count = 1

    for line in sys.stdin:
        line = line.strip()

        runner_key, runner_image = line.split("\t", 1)

        if current_key == runner_key:
            current_image = current_image + "," + runner_image
            count = count + 1
        
        else:
            if current_key:
                print("%s\t%d\t%s" % (current_key, count, current_image))
                count = 1

            current_key = runner_key
            current_image = runner_image

    if current_key == runner_key:
        print("%s\t%d\t%s" % (current_key, count, current_image))


if __name__ == "__main__":
    main()