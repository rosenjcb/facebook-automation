from page import BasePage
from appium.webdriver.common.touch_action import TouchAction

class HomePage(BasePage):
    def click_camera_icon(self):
        buttons = self.driver.find_elements_by_class_name("android.widget.Button")
        not_now_button = [x for x in buttons if "Not Now" == x.text][0]
        not_now_button.click()
        print "not now button clicked"

        camera_button = self.driver.find_element_by_accessibility_id("Camera")
        camera_button.click()
        print "camera button clicked"

    def click_options_menu(self):
        #more_button = self.driver.find_element_by_accessibility_id("More, Tab 5 of 5")
        more_button= self.driver.find_element_by_xpath("//android.widget.FrameLayout[@index=2]/android.widget.LinearLayout[@index=0]/android.widget.FrameLayout[@index=4]")
        #more_button.click()
        actions = TouchAction(self.driver)
        actions.tap(more_button)
        actions.perform()
        print "options menu clicked"