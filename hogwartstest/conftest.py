# -------------------------------------------------------------------------------
# Name:         pytest第一次直播课作业
# Description:
# Author:       zhangdonghui
# Date:         2020/6/26
# -------------------------------------------------------------------------------
import pytest
from hogwartstest.calculator import *


@pytest.fixture(autouse=True)
def start_calc():
    print("开始计算")
    calc = Calc()
    yield calc
    print("计算结束")


# -------------------------------------------------------------------------------
# Name:         pytest第二次直播课作业
# Description:
# Author:       zhangdonghui
# Date:         2020/6/27
# -------------------------------------------------------------------------------
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env')


@pytest.fixture(scope='session')
def cmddoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        print("获取测试数据")
        with open('/data/test.yml') as f:
            data = yaml.safe_load(f)
    elif myenv == 'dev':
        print("获取生产数据")
        with open('/data/dev.yml') as f:
            data = yaml.safe_load(f)
    elif myenv == 'st':
        print("获取系统数据")
        with open('/data/st.yml') as f:
            data = yaml.safe_load(f)
    return data
