# coding:utf-8
import time
from appium import webdriver
import  unittest
import  HTMLTestRunner
import time


class TestLogin(unittest.TestCase):
    def setUp(self):
        #初始化
        desired_caps = {}
        # 使用哪种移动平台
        desired_caps['platformName'] = 'Android'
        # Android版本
        desired_caps['platformVersion'] = '7.1.1'
        # 启动哪种设备，是真机还是模拟器？
        desired_caps['deviceName'] = 'L041807000058'
        #App的绝对路径
        #desired_caps['app'] = 'C:\\Users\\Administrator\\Downloads\\appstudent-release.apk' # 指向.apk文件，如果设置appPackage和appActivity，那么这项会被忽略
        desired_caps['appPackage'] = 'com.strong.leke.student'#包名
        desired_caps['appActivity'] = 'com.strong.leke.student.app.activity.WelcomeActivity'#Activity名
        desired_caps['unicodeKeyboard'] = True  # 使用unicodeKeyboard的编码方式来发送字符串
        desired_caps['resetKeyboard'] = True  # 将键盘给隐藏起来

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# WebDriverWait(driver, 20).until(lambda the_driver: the_driver.find_element_by_id("com.strong.leke.student:id/tv_login").is_displayed())
    def testDown(self):
        time.sleep(10)
        self.driver.quit()


    def test_login(self):
        login =self.driver.find_element_by_id("com.strong.leke.student:id/login_username")
        time.sleep(50)
        login.send_keys('187340')
        # 输入密码
        self.driver.find_element_by_id("com.strong.leke.student:id/login_password").send_keys('123456aa')
        # 点击登录
        self.driver.find_element_by_id("com.strong.leke.student:id/btn_login").click()
        result = self.driver.find_element_by_id("com.strong.leke.student:id/tv_home_title").text
        time.sleep(50)
        self.assertEqual(result, "校园课堂")









