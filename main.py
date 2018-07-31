# This is a demo automation for Instagram to log in to the app, take a photo, save to the gallery and then logout.
import unittest
from time import sleep
import time

from appium import webdriver

import gallery_page
import home_page
import login_page
import options_page
#import profile_page

""" 
The appActivity for the login was found via adb. I opened the Facebook app on my phone and then ran two commands: 

adb shell
dumpsys window windows | grep -E 'mCurrentFocus'

The first command logged me into the shell of my device and then I was able to run a second command 
to grab the system services and filter for the currently focused activity (i.e. Facebook's login page).

I also used aapt to read the manifest file of the Facebook apk file and find the launcher activity (the grep command earlier
would not give me the correct activity to launch with).
"""

class FacebookTest(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {'platformName': 'Android', 'platformVersion': '8.1.0',
                        'deviceName': 'HT8321A00080', 'appPackage': 'com.facebook.katana',
                        'appActivity': 'com.facebook.katana.LoginActivity', 'autoGrantPermissions': 'true'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
        self.driver.implicitly_wait(10)

    def test_automation(self):

        login = login_page.LoginPage(self.driver)
        login.do_login()

        home = home_page.HomePage(self.driver)
        #self.assertEqual(home.verify_home_page(), 'True')
        home.click_camera_icon()

        gallery = gallery_page.GalleryPage(self.driver)
        gallery.click_and_save_image()

        home = home_page.HomePage(self.driver)
        home.click_options_menu()

        options = options_page.OptionsPage(self.driver)
        options.swipe_to_bottom()
        options.log_out()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()