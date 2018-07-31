from page import BasePage


class LoginPage(BasePage):
    def do_login(self):
        #Google Smart Lock always appears when I open Facebook, so I have to cancel out of that to do a regular login. 
        #cancel_button = self.driver.find_element_by_id("com.google.android.gms:id/cancel")
        #cancel_button.click()


        #Resource-IDs are hidden, so we create a list of all the elements containing of a specific class. Then we iterate
        #through the list and return the member that contains the text of the element we are looking for. 
        text_fields = self.driver.find_elements_by_class_name("android.widget.EditText")
        user_name = [x for x in text_fields if "Phone or Email" == x.text][0]
        user_name.click()
        user_name.clear()
        user_name.send_keys("facebookautomationtest@gmail.com")
        print "username entered"
        self.driver.back()

        password = [x for x in text_fields if "Password" == x.text][0]
        password.click()
        password.clear()
        password.send_keys("FacebookNow22")
        print "password entered"

        buttons = self.driver.find_elements_by_class_name("android.widget.Button")
        log_in_button = [x for x in buttons if "LOG IN" == x.text][0]
        log_in_button.click()
        print "log in button clicked"