# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys
sys.path.append('C:\\Users\\Lenovo\\.jenkins\\workspace\\appium')

import unittest
from dianji.test1 import MyTestCase
from dianji.test2 import MyTestCase2
import HTMLTestRunner
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(MyTestCase))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(MyTestCase2))



    #suite.addTest(unittest.TestLoader().loadTestsFromTestCase(ceshi1))
    # 这一步是在当前文件夹里自动生成一个测试报告
    with open('../baogao/HTMLReport.html', 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)