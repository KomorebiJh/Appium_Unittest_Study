import time
import unittest

from appium import webdriver


class MyTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '5.1.1',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.android.browser',  # apk的包名
                        'appActivity': 'com.android.browser.BrowserActivity'  # activity 名称
                       }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(10)

    def test_borswer(self):

        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
            '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget'
            '.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit'
            '.WebView/android.view.View[2]/android.view.View[3]/android.view.'
            'View/android.widget.EditText').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                          '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget'
                                          '.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit'
                                          '.WebView/android.view.View[2]/android.view.View[3]/android.view.'
                                          'View/android.widget.EditText').clear()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                          '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget'
                                          '.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit'
                                          '.WebView/android.view.View[2]/android.view.View[3]/android.view.'
                                          'View/android.widget.EditText').send_keys('搜狗输入法')
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.'
                                          'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.'
                                          'LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.'
                                          'view.View[2]/android.view.View[3]/android.view.View/android.'
                                          'widget.Button').click()
        self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
                                          'android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.'
                                          'widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.'
                                          'view.View[2]/android.widget.ListView/android.view.'
                                          'View[1]/android.view.View[1]').click()
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[3]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[2]').click()
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ResolverDrawerLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView').click()
        # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ResolverDrawerLayout/android.widget.LinearLayout[2]/android.widget.Button[1]').click()
        #
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()



