import subprocess
import glob
import os
from appium import webdriver
import sys, os, time

desired_cap = {
    "platformName": "Android",
    "deviceName": "7989a582",
    # "app": "C:\  .apk"
    # Please search for wireless access
}

print("Connecting to IHU...")
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(2000)
print("Connection Success!...")
driver.wait_activity('Wait', 2)


# launch the SML
def script_start():
    print("Launching the SML app...")
    driver.wait_activity('Wait', 2)
    driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Share My Location"]').click()

    # Select the Number tab
    print("Clicking on Number tab...")
    driver.wait_activity('Wait', 2)
    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                 '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view'
                                 '.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout['
                                 '4]/android.widget.FrameLayout/android.widget.TextView').click()

    # Entering the Number
    print("Entering the default Number...")
    driver.wait_activity('Wait', 3)
    number = driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
        '.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget'
        '.FrameLayout/android.view.ViewGroup/android.widget.EditText')
    number.send_keys('73505892')

    print("Clicking on 5...")
    driver.wait_activity('Wait', 1)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
        '.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget'
        '.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button['
        '6]').click()

    # Send SMS
    print("Clicking on Send...")
    driver.wait_activity('Wait', 3)
    driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
        '.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget'
        '.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button['
        '11]').click()

    # Click Share
    print("Sharing in progress...")
    driver.wait_activity('Wait', 3)
    driver.find_element_by_id('com.lynkco.connected.incar.sharemylocation:id/btnPositive').click()


# Success Logs
def log_analysis():
    print("Analysing the logs file...")
    driver.wait_activity('Wait', 7)

    os.chdir(r'C:\Users\nikhil.tamboli\Desktop\ConnectivityProj\Logs\0704')
    for file_txt in glob.glob("*.txt"):
        print(file_txt)
        with open(file_txt, 'r', encoding='Latin-1') as currentFile:
            text = currentFile.read()
            if "handleStateChange: SUCCESS" in text:
                print("Message sent successfully")
            else:
                print("Message not sent!")


# Logs collection
def collect_logs():
    print("Starting the logs file...")
    driver.wait_activity('Wait', 2)
    subprocess.call("adb logcat > SML_0604.txt", shell=True)


def main():

    print("Inside Main...")

    for i in range(3):
        print("================= Test Cycle", i+1, "Started ================")
        # collect_logs()
        script_start()
        log_analysis()

    print("==========Total", i+1, "testing cycles completed ============")


if __name__ == "__main__":
    main()
