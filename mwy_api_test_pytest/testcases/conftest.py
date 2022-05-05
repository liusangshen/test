# import pytest
# from common.Base import BaseTest
#
#
# # 用例级别的前置
# @pytest.fixture(scope='function')
# def case_setup():
#     # 执行测试用例前：先调用登录方法
#     BaseTest.login()
#
#     yield
#
#     # 执行测试用后：执行
#     print('用例执行完毕')
#
#
# # 测试类级别的前置
# @pytest.fixture(scope='class', autouse=True)
# def cls_setup():
#     print("--------测试类级别的前置方法------------")
#
#     yield
#
#     print("--------测试类级别的后置方法------------")

