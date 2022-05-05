import os
import pytest
from common.Base import BaseTest
from requests import request
from common.Handle_config import conf


class TestLoginOut(BaseTest):
    cases = BaseTest().cases('mwy_shop_login.xlsx', 'loginout')

    # # 每次用例执行前：执行一次登录操作
    # def setUp(self):
    #     self.login()

    @pytest.mark.run(order=-2)
    @pytest.mark.parametrize('item', cases)
    def test_loginout(self, item):
        # 第一步：测试前数据准备
        # 用例标题
        title = item['title']
        # 请求地址
        url = os.path.join(eval(conf.get('mwy', 'sys_url')) + '/loginout')
        # 请求方式
        method = item['method'].lower()
        # 请求头
        headers = eval(conf.get('mwy', 'headers'))
        # 预期结果
        excepted = eval(item['excepted'])
        # 第二步：调用被测接口，获取实际结果
        response = request(method=method, url=url, headers=headers)
        res = response.json()
        print("预期结果：", excepted)
        print("实际结果：", res)
        # 第三步：断言
        self.assert_try(excepted, res, title)


if __name__ == "__main__":
    pytest.main()
