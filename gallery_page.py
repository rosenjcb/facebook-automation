from page import BasePage


class GalleryPage(BasePage):

    def click_and_save_image(self):
        camera_button = self.driver.find_element_by_accessibility_id("Take photo or hold for video")
        camera_button.click()
        print "camera shutter clicked"

        camera_save = self.driver.find_element_by_accessibility_id("Share on next screen")
        camera_save.click()
        print "camera save button clicked"

        now_button = self.driver.find_element_by_accessibility_id("SHARE NOW")
        now_button.click()
        print "now button clicked"
