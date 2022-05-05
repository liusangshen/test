import pytest
import os
from requests import request
from common.Base import BaseTest
from common.Handle_config import conf


class TestUpdatePwd(BaseTest):
    cases = BaseTest().cases('mwy_shop_login.xlsx', 'updatepwd')

    def setUp(self):
        # 测试用例执行前：先登录
        self.login()

    # 登录后：执行修改密码的测试用例
    @pytest.mark.parametrize('item', cases)
    def test_update_pwd(self, item):
        # 第一步：测试前数据准备
        # 用例标题
        title = item['title']
        # 请求地址
        url = os.path.join(eval(conf.get('mwy', 'sys_url')) + item['url'])
        # 请求方式
        method = item['method']
        # 请求头
        headers = eval(conf.get('mwy', 'headers'))
        # 请求参数
        data = eval(item['data'])
        # 预期结果
        excepted = eval(item['excepted'])
        # 第二步：调用被测接口，获取接口返回数据
        response = request(method=method, url=url, headers=headers, json=data)
        res = response.json()
        print("预期结果：", excepted)
        print("实际结果：", res)
        # 第三步：断言
        self.assert_try(excepted, res, title)


if __name__ == "__main__":
    pytest.main()
