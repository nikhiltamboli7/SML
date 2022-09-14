import subprocess
from PIL import Image
from PIL import ImageChops
import sys, os, time

def compare_img():
        print("Hello from compare function")

        subprocess.call(
            "adb exec-out screencap -p > C:\\Users\\nikhil.tamboli\\Desktop\\ConnectivityProj\\automation\\cropped_img\\screen.png",
            shell=True)
        print("image saved at directory")
        ref_img = Image.open(r'C:\Users\nikhil.tamboli\Desktop\ConnectivityProj\automation\ref_img\signIn.png')
        crop_img = Image.open('C:\\Users\\nikhil.tamboli\\Desktop\\ConnectivityProj\\automation\cropped_img\\screen.png')

        if list(crop_img.getdata()) == list(ref_img.getdata()):
            print("Image Identical...Test case PASS")
        else:
            print("Images not matching...Test case FAILED")


compare_img()