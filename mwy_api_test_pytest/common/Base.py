import os
import requests
import jsonpath
from common.Handle_config import conf
from common.Handle_log import my_log
from common.Handle_path import DATA_DIR
from common.Handle_excel import HandleExcel


class BaseTest:

    # 通用：登录成功方法
    @classmethod
    def login(cls):
        url = os.path.join(eval(conf.get('mwy', 'sys_url')) + '/login')
        # 请求头
        headers = eval(conf.get('mwy', 'headers_login'))
        # 请求参数
        data = eval(conf.get("mwy", 'data'))
        # 预期结果
        excepted = {'returnCode': '000000', 'returnMsg': '成功'}
        # 第二步：调用功能函数，获取实际结果
        response = requests.post(url=url, headers=headers, json=data)

    # 获取部门id
    @classmethod
    def department(cls):
        cls.login()
        url = eval(conf.get('mwy', 'sys_url')) + '/shop/department/page'
        headers = eval(conf.get('mwy', 'headers'))
        data = {"pageNum": 1,
                "pageSize": 10,
                "parentId": 0,
                "name": "测试部门"}
        # 调用被测接口，获取请求结果
        response = requests.post(url=url, headers=headers, json=data)
        res = response.json()
        department_id = jsonpath.jsonpath(res, '$..id')[0]
        return department_id

    # 通用：断言方法
    @classmethod
    def assert_try(cls, excepted, res, title):
        assert excepted['returnCode'] == res['returnCode']
        try:
            assert excepted['returnCode'] == res['returnCode']
            assert excepted['returnMsg'] == res['returnMsg']
        except AssertionError as e:
            my_log.error("用例-----{0}-----执行失败".format(title))
            my_log.Exception(e)
            raise e
        else:
            my_log.info("用例-----{0}-----执行通过".format(title))

    # 通用：获取excel数据方法
    @classmethod
    def cases(cls, file_name, sheet_name):
        execl = HandleExcel(os.path.join(DATA_DIR, file_name), sheet_name)
        cases = execl.data_read()
        return cases


if __name__ == "__main__":
    ids = BaseTest().department()
    print(ids)
