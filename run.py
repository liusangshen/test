"""
=============================
Author:sangshen
time:2022/2/15 
E-mail:928857196@qq.com 
=============================
"""
import unittest
from common.Handle_path import CASE_DIR, REPORT_DIR
from unittestreport import TestRunner


def main():
    suit = unittest.defaultTestLoader.discover(CASE_DIR)
    runner = TestRunner(suit,
                        filename="report.html",
                        report_dir=REPORT_DIR,
                        title='测试报告',
                        tester='桑葚',
                        desc="测试报告",
                        )
    # 执行所有测试用例
    runner.run()

    # 将测试用例的执行结果发送到邮箱
    runner.send_email(host="smtp.qq.com",
                      port=465,
                      user="928857196@qq.com",
                      password="xnscqflxgwpybecj",
                      to_addrs="928857196@qq.com",
                      is_file=True)


if __name__ == "__main__":
    main()
