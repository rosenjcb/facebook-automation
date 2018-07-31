from page import BasePage

class OptionsPage(BasePage):
    def swipe_to_bottom(self):
        for x in range(0, 20):
            self.driver.swipe(100, 0, 100, 500)
        print "swiped to bottom of page"

    def log_out(self):
        log_out_button = self.driver.find_element_by_accessibility_id("Your Profile")
        log_out_button.click()
        print "logged out"

