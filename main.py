import unittest
import  HTMLTestRunner
import time
import os


if __name__ == '__main__':
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover("./", '*.py')

    for case in discover:
        suite.addTest(case)
    print(discover)

    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    day  = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    result_path = "./report" + "//"
    report_file = result_path + "index.html"
    fp  = open(report_file,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"appium测试报告",description=u'用例详情;')
    runner.run(suite)
    fp.close()



