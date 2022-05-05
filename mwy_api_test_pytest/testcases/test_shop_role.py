import pytest
from requests import request
from common.Handle_config import conf
from common.Base import BaseTest


class TestShopRole(BaseTest):
    # 获取分页文件
    cases1 = BaseTest().cases('mwy_shop_role.xlsx', 'page')

    @classmethod
    def setUpClass(cls):
        cls.login()

    # 查询门店角色
    @pytest.mark.parametrize('item', cases1)
    def test_shop_role_1_page(self, item):
        # 第一步：测试前数据准备
        # 用例标题
        title = item['title']
        # 请求地址
        url = eval(conf.get('mwy', 'sys_url')) + item['url']
        # 请求方式
        method = item['method']
        # 请求头
        headers = eval(conf.get('mwy', 'headers'))
        # 请求参数
        data = eval(item['data'])
        # 预期结果
        excepted = eval(item['excepted'])
        # 第二步：调用被测接口，获取实际结果
        response = request(method=method, url=url, headers=headers, json=data)
        res = response.json()
        print("预期结果：", excepted)
        # print("实际结果", res)
        # 第三步：断言
        self.assert_try(excepted, res, title)

    # 新增门店角色
    def test_shop_role_2_add(self):
        pass

    # 修改门店角色
    def test_shop_role_3_update(self):
        pass

    # 删除门店角色
    def test_shop_role_4_delete(self):
        pass


if __name__ == "__main__":
    pytest.main()
