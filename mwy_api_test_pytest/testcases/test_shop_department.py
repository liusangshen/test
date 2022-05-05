import pytest
import requests
from common.Base import BaseTest
from common.Handle_config import conf


class TestRDeportment(BaseTest):
    # 分页文件读取
    cases1 = BaseTest().cases('mwy_shop_department.xlsx', 'page')

    # 新增文件读取
    cases2 = BaseTest().cases('mwy_shop_department.xlsx', 'add')

    # 修改文件读取
    cases3 = BaseTest().cases('mwy_shop_department.xlsx', 'update')

    # 读取删除文件
    cases4 = BaseTest().cases('mwy_shop_department.xlsx', 'delete')

    @classmethod
    def setUpClass(cls):
        # 所有的用例执行前：执行一次登录
        cls.login()

    # 分页获取部门信息
    @pytest.mark.parametrize('item', cases1)
    def test_department_1_page(self, item):
        # 第一步：测试前数据准备
        # 用例标题
        title = item['title']
        # 请求地址
        url = eval(conf.get('mwy', 'sys_url')) + item['url']
        # 请求方式
        method = item['method'].lower()
        # 请求头
        headers = eval(conf.get('mwy', 'headers'))
        # 请求参数
        data = eval(item['data'])
        # 预期结果
        excepted = eval(item['excepted'])
        # 第二步：调用被测接口，获取实际结果
        response = requests.request(method=method, url=url, headers=headers, json=data)
        res = response.json()
        print('预期结果：', excepted)
        print('实际结果：', res)
        # 第三步：断言
        self.assert_try(excepted, res, title)

    # 新增顶级部门
    @pytest.mark.parametrize('item', cases2)
    def test_department_2_add_top(self, item):
        # 第一步：测试前数据准备
        # 用例标题
        title = item['title']
        # 请求地址
        url = eval(conf.get('mwy', 'sys_url')) + item['url']
        headers = eval(conf.get('mwy', 'headers'))
        data = eval(item['data'])
        excepted = eval(item['excepted'])
        method = item['method'].lower()
        # 第二步：调用被测接口，获取实际结果
        response = requests.request(method=method, url=url, headers=headers, json=data)
        res = response.json()
        print('预期结果：', excepted)
        print('实际结果：', res)
        # 第三步：断言
        self.assert_try(excepted, res, title)

    # 修改部门信息
    @pytest.mark.parametrize('item', cases3)
    def test_department_3_update(self, item):
        # 修改部门信息：前置获取对应的部门id
        department_id = self.department()
        print(department_id)
        # 第一步：测试前数据准备
        # 用例标题
        title = item['title']
        # 请求地址
        url = eval(conf.get('mwy', 'sys_url')) + item['url']
        headers = eval(conf.get('mwy', 'headers'))
        data = item['data']
        print(data)
        data = eval(data.replace('#id#', str(department_id)))
        print(data)
        method = item['method'].lower()
        excepted = eval(item['excepted'])
        # 第二步：调用被测接口，获取实际结果
        response = requests.request(method=method, url=url, headers=headers, json=data)
        res = response.json()
        print('预期结果：', excepted)
        print('实际结果：', res)
        # 第三步：断言
        self.assert_try(excepted, res, title)

    # 删除顶级部门
    @pytest.mark.parametrize('item', cases4)
    def test_department_4_del(self, item):
        # 删除部门：前置获取对应的部门id
        department_id = self.department()
        # 第一步：测试前数据准备
        # 用例标题
        title = item['title']
        url = eval(conf.get('mwy', 'sys_url')) + item['url']
        url = str(url).replace('#{id}#', str(department_id))
        headers = eval(conf.get('mwy', 'headers'))
        method = item['method'].lower()
        excepted = eval(item['excepted'])
        # 第二步：调用被测接口，获取实际结果
        response = requests.request(method=method, url=url, headers=headers)
        res = response.json()
        print("预期结果：", excepted)
        print("实际结果：", res)
        # 断言
        self.assert_try(excepted, res, title)


if __name__ == "__main__":
    pytest.main()
