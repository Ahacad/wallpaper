#! /usr/bin/env python3

import os


path = "/home/ahacad/Workstation/Prepared/wallpaper/Great/"
for item in os.listdir(path):
    if len(item) > 15:
        name = item.split(".")[1]
        name = int(name) + 101
        name = str(name)
        os.rename(path + item, path + name)
