"""
=============================
Author:sangshen
time:2022/2/15 
E-mail:928857196@qq.com 
=============================
"""
import pytest

pytest.main(['testcases/', '-s', '-v',
             # '--reruns', '3',
             # '--reruns-delay', '2',
             '--alluredir=allure_report'
             ])
