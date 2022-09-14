from appium import webdriver
import subprocess
from PIL import Image
from PIL import ImageChops
import sys, os, time

desired_cap = {
    "platformName": "Android",
    "deviceName": "7989a582",
    #"app": "C:\meetings-0.1.0-543-release-220324-0919.apk"
}

# Imge comaparision function
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


print("Wait! Connecting to IHU...")
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(2000)
print("Connection Success!...")
driver.wait_activity('Wait', 2)


print("Launching the meeting app...")
driver.wait_activity('Wait', 3)
driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Meetings"]').click()  # Launch Meeting
driver.wait_activity('Wait', 1)
compare_img()
driver.wait_activity('Wait', 1)


print("Clicking on SignIn...")
driver.wait_activity('Wait', 3)
driver.find_element_by_id('com.lynkco.connected.incar.meetings:id/signInButton').click()  # SignIn button

print("Clicking on Profile")
driver.wait_activity('Wait', 3)
driver.find_element_by_xpath(
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]').click()  # Profile click

print("Clicking on SignIn...")
driver.wait_activity('Wait', 3)
driver.find_element_by_xpath(
    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button[2]').click()  # Click Sign-In

print("Entering the password...")
driver.wait_activity('Wait', 3)
password = driver.find_element_by_xpath(
    '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.EditText[2]')
password.send_keys('abcd@1234')

print("Clicking on OK")
driver.wait_activity('Wait', 3)
driver.find_element_by_id('se.cevt.profilemanager:id/btn_ok').click()


print("===================You are now signed In. Execution completed!===========================")




# Locate element by using Class name

'''
comment part
'''
# Locate element by using image
