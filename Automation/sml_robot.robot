*** Settings ***

Library  AppiumLibrary


*** Variables ***


*** Test Cases ***
Open Application On Android

    Open Application    http://localhost:4723/wd/hub    platformName=Android    udid=192.168.137.86:5555    appPackage=com.lynkco.connected.incar.sharemylocation   appActivity=ui.screens.main.MainActivity   automationName=Uiautomator2
    Wait Activity   ui.screens.main.MainActivity   timeout=8   interval=1
    #AppiumLibrary.Capture Page Screenshot     Login.png

CLick Dialpad
    #Click Element   id=com.lynkco.connected.incar.sharemylocation:id/buttonText
    Click Text  Number  exact_match = True

Enter number
    #Input Value     class=android.widget.EditText   735058926
    #Click Text  6  exact_match = True
    Click Element  id=com.lynkco.connected.incar.sharemylocation:id/button_7
    Click Text  3   exact_match=False

Enable send
    Element Should Be Enabled   class=android.widget.Button
CLick Send
    Click button    Send
CLick Send2
    Click button    Send
Sent success
    Wait Until Page Contains    Failed   error=None


CLick LastSent
    #Click Element   id=com.lynkco.connected.incar.sharemylocation:id/categoryImage
    Click Text  Last sent  exact_match = False

CLick contacts
    #Click Element   id=com.lynkco.connected.incar.sharemylocation:id/buttonText
    Click Text  Phone contacts  exact_match = False

Click favorites_rsrc id
    #Click Element   id=com.lynkco.connected.incar.sharemylocation:id/favoriteContactsFragment
    Click Text  Saved  exact_match = True


*** Keywords ***
