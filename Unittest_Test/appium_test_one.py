import sys
import unittest
import time
from importlib import reload
import logging
from appium import webdriver
import HTMLTestRunner



logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
# 统一使用utf-8格式


class MyTestCase(unittest.TestCase):

    @classmethod

    def setUp(self):
        logger.info("开始")
        desired_caps = {'platformName':'Android',
                        'platformVersion':'8.1.0',
                        'deviceName':'ENU7N15A12000064',
                        'appPackage':'com.yue.customcamera',
                        'appActivity':'MainActivity'
                        }
        logger.info("连接Appnium")
        self.driver = webdriver.RemoteWebDriver("http://127.0.0.1:4723/wd/hub",desired_caps)
        logger.info("连接Appnium2")
        self.driver.implicitly_wait(8)

        print("-------------Setup----------")

    def tearDown(self):
            logger.info("结束")
            print("----------teardown")

    def paishe(self):
        try:
            self.test_login()
            self.test_video()
            self.test_listvideo()
            self.test_photograph()
        except Exception as e:
            print("Exception !\n",e)
            self.test_failed()
            raise

    def test_failed(self):
        now2 = time.strftime("%H%M%S", time.localtime())
        logger.error("出现错误！！！")
        picture = now + "error" + now2 + ".jpg"
        self.driver.get_screenshot_as_file(picture)


    def test_login(self, now1=None):
        ow1 = time.strftime("%Y%m%d%H%M%S", time.localtime())
        logger.info("输入用户名称")
        self.driver.find_element_by_id("com.yue.customcamera:id/userName").send_keys("huangpeng")  # 登录页输入账号
        time.sleep(2)

        logger.info("输入文物名称")
        self.driver.find_element_by_xpath("//*[@resource-id='com.yue.customcamera:id/articleName']").send_keys(
            "article" + now1)
        time.sleep(2)

        logger.info("开始采集")
        self.driver.find_element_by_id("com.yue.customcamera:id/startMine").click()  # 开始采集
        time.sleep(2)

        # 断言
        self.assertEqual('录像时间:%s', self.driver.find_element_by_id("com.yue.customcamera:id/recordTime").text)


    def test_video(self):

        logger.info("录像")
        for count in list(range(1, 2)):
            # logger.info("第" + str(count) + "次录像")
            self.driver.find_element_by_xpath("//*[@resource-id='com.yue.customcamera:id/img_video_shutter']").click()
            time.sleep(1)
            while True:  # 循环判断录像是否完成
                try:
                    self.driver.find_element_by_id('com.yue.customcamera:id/title')
                    logger.info("录像完成")
                    break
                except:
                    logger.info("录像中…")
                    time.sleep(2)

    def test_listvideo(self):

        adds = ['20秒','40秒','50秒','1分','1分10秒','1分20秒','1分30秒','1分40秒','1分50秒',]
        for add in adds:
            logger.info("录制视频"+add)
            self.driver.swipe(691,1221,570,1221,500)
            time.sleep(2)
            self.test_video()
            time.sleep(2)



    def test_photograph(self):
        logger.info("进入拍照")
        self.driver.find_element_by_xpath("//*[@resource-id='com.yue.customcamera:id/take_camera']").click()
        for count in list(range(1, 41)):
            logger.info("第" + str(count) + "次拍照")
            self.driver.find_element_by_xpath("//*[@resource-id='com.yue.customcamera:id/photoImgBtn']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.yue.customcamera:id/savePics']").click()

        # 断言
        self.assertEqual('当前拍照数目：0', self.driver.find_element_by_id("com.yue.customcamera:id/currentDirPicNum").text)


    def test_something(self):
        self.assertEqual(True, False)





if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyTestCase('test_paishe'))

    now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    filename = "_ReportCase.html"
    print('run version {}'.format(sys.version))
    fp = open(now + filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u"TestCase Report")
    runner.run(suite)
    fp.close()

