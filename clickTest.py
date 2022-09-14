from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "deviceName": "7989a582",
    #"app": "C:\  .apk"
}

print("Connecting to IHU...")
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(2000)
print("Connection Success!...")
driver.wait_activity('Wait', 2)

print("Launching the SML app...")
driver.wait_activity('Wait', 2)
driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Share My Location"]').click()


print("Clicking on 5...")
driver.wait_activity('Wait', 1)
driver.find_element_by_id('com.lynkco.connected.incar.sharemylocation:id/button_5').click()
