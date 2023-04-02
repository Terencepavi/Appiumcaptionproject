import time

from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.nativekey import AndroidKey
from base.appium_listner import AppiumConfig


class TestAndroidDeviceLocal(AppiumConfig):
    def test_uninstall_app(self):
        if self.driver.is_app_installed("com.flipkart.android"):
            self.driver.remove_app("com.flipkart.android")

    def test_Choose_lang_enter_invalid_email_verify_error(self):
        print(self.driver.page_source)
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='English']").click()
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='CONTINUE']").click()
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Use Email-ID']").click()
        self.driver.find_element(AppiumBy.ID,"com.flipkart.android:id/phone_input").send_keys("abc123@email.com")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='CONTINUE']").click()
        errormsg=self.driver.find_element(AppiumBy.ID,"com.flipkart.android:id/tv_error_message").text
        assert_that(errormsg).is_equal_to('Your Flipkart account has been blocked. Please contact our customer support to fix this.')
        self.driver.find_element(AppiumBy.ID,'com.flipkart.android:id/custom_back_icon').click()
        time.sleep(20)

    def test_search_products(self):
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Search for products']").click()
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@text='Search for Products, Brands and More']").send_keys("Iphone")
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='iphone 13']").click()
        # scroll to APPLE iPhone 14 and click
        mobile_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("APPLE iPhone 14 ((PRODUCT)RED, 256 GB)")'}
        self.driver.execute_script("mobile: scroll", mobile_dic)
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='APPLE iPhone 14 ((PRODUCT)RED, 256 GB)']").click()
        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR,"selector": 'UiSelector().text("APPLE iPhone 14 ((PRODUCT)RED, 256 GB)")'}
        self.driver.execute_script("mobile: scroll", para_dic)
        viewpagetext=self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='APPLE iPhone 14 ((PRODUCT)RED, 256 GB)']").text
        assert_that(viewpagetext).is_equal_to('APPLE iPhone 14 ((PRODUCT)RED, 256 GB)')

    def test_verify_cart(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Cart")').click()
        cart_empty_msg = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Missing Cart items?")').get_attribute("displayed")
        assert_that(cart_empty_msg).is_equal_to('true')

    def test_verify_notification(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Notifications")').click()
        notification_empty_msg = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign In  ")').get_attribute("enabled")
        assert_that( notification_empty_msg).is_equal_to('true')

    def test_scroll_homepage_buy_now(self):
        # scroll to art of asia and click
        homepage = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("Shop for a Cool Summer")'}
        self.driver.execute_script("mobile: scroll",homepage)

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Shop for a Cool Summer']").click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Emergency Lights")').click()
        wiprolight = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("Wipro 6W Re-chargeable LED Table Lamp 4 hrs Lantern Emergency Light, White")'}
        self.driver.execute_script("mobile: scroll", wiprolight)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Wipro 6W Re-chargeable LED Table Lamp 4 hrs Lantern Emergency Light, White")').click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Buy now']").click()
        login_erro_msg=self.driver.find_element(AppiumBy.ID,"com.flipkart.android:id/title").text
        assert_that(login_erro_msg).is_equal_to("Log in to complete your shopping")









    