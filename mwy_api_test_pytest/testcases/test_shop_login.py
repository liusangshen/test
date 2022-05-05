import pytest
import requests
from common.Handle_config import conf
from common.Base import BaseTest


class TestLogin(BaseTest):

    # 读取文件数据
    cases1 = BaseTest().cases('mwy_shop_login.xlsx', 'login_success')
    cases2 = BaseTest().cases('mwy_shop_login.xlsx', 'login_fail')
    headers = eval(conf.get("mwy", "headers_login"))

    # 登录满屋云门店后台
    @pytest.mark.parametrize('item', cases1)
    def test_login_success(self, item):
        # 第一步：测试前数据准备
        # 请求用例标题
        title = item['title']
        # 请求地址
        url = eval(conf.get('mwy', 'sys_url')) + item["url"]
        # 请求参数
        params = eval(item["data"])
        # 请求方式
        method = item["method"].lower()
        # 预期结果
        excepted = eval(item["excepted"])
        # 第二步：调用被测接口，获取实际结果
        response = requests.request(method=method, url=url, headers=self.headers, json=params)
        res = response.json()
        print("预期结果：{0}".format(excepted))
        # print("实际结果：{0}".format(res))
        # 第三步：断言
        self.assert_try(excepted, res, title)

    # 登录满屋云门店后台
    @pytest.mark.parametrize('item', cases2)
    def test_login_fail(self, item):
        # 第一步：测试前数据准备
        # 请求用例标题
        title = item['title']
        # 请求地址
        url = eval(conf.get('mwy', 'sys_url')) + item["url"]
        # 请求参数
        params = eval(item["data"])
        # 请求方式
        method = item["method"].lower()
        # 预期结果
        excepted = eval(item["excepted"])
        # 第二步：调用被测接口，获取实际结果
        response = requests.request(method=method, url=url, headers=self.headers, json=params)
        res = response.json()
        print("预期结果：", excepted)
        print("实际结果：", res)
        # 第三步：断言
        self.assert_try(excepted, res, title)


if __name__ == "__main__":
    pytest.main()
