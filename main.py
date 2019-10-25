import unittest
import  HTMLTestRunner
import time


if __name__ == '__main__':
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover("F:\\Python\\TestLoginCase\\", '*.py')

    for case in discover:
        suite.addTests(case)
    # suite.addTest(TestLogin_0

    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    day  = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    result_path = "F:\\Report\\"
    report_file = result_path + "\\"+ now + "_result.html"
    fp  = open(report_file,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"appium测试报告",description=u'用例详情;')
    runner.run(suite)
    fp.close()



