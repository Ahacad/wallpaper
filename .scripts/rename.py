import os

for fil in os.listdir("/home/ahacad/Workstation/Prepared/wallpaper/Great"):
    if len(fil) > 15:
        num = int(fil.split('.')[1]) + 5
        os.rename(fil, str(num))
