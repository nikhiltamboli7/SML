from appium import webdriver


desired_cap = {
  "platformName": "Android",
  "deviceName": "7989a582",
  "app": "C:\meetings-0.1.0-543-release-220324-0919.apk"
}

desired_cap = {
    "platformName": "Android",
    "deviceName": "7989a582",
    "appPackage": "com.spotify.music",
    "appActivity": "com.spotify.auto.ui.login.AAMLoginScannableActivity",
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.find_element_by_name("Meetings")
ref_img = driver.find_element_by_image("C:\Users\nikhil.tamboli\Desktop\ConnectivityProj\automation\signIn")