"""
discover() 匹配某目录下的所有测试用例。
"""
import os
from HTMLTestRunner import *


if __name__ == '__main__':
    report_dir = './report/'
    if not os.path.isdir(report_dir):
        os.makedirs(report_dir)
    # 导入当前时间，使用time模块的相关函数
    now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    report_path = report_dir + now + 'htmlreport.html'

    suite = unittest.TestSuite()  # 创建测试套件
    # 找到某个目录下所有的以test开头的Python文件里面的测试用例
    all_cases = unittest.defaultTestLoader.discover("./test_case", pattern='test_*.py')
    for case in all_cases:
        suite.addTests(case)  # 把所有的测试用例添加进来

    fp = open(report_path, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='所有测试情况')
    runner.run(suite)
    fp.close()
