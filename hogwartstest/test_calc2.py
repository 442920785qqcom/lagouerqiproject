# -------------------------------------------------------------------------------
# Name:         pytest第二节直播课作业
# Description:
# Author:       zhangdonghui
# Date:         2020/6/27..
# -------------------------------------------------------------------------------
from hogwartstest.calculator import *
import pytest
import yaml

with open("calculator_data2.yml") as f:
    data = yaml.safe_load(f)


class Testcal:

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,result', data['minus1'],
                             ids=["int", "float", "bignum", "minus", "float+int"])
    @pytest.mark.dependency(depends=["add"])
    def check_minus(self, start_calc, a, b, result):
        assert result == start_calc.minus(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name="mul")
    @pytest.mark.parametrize('a,b,result', data['mul1'],
                             ids=["int", "float", "bignum", "minus", "float+int"])
    def check_mul(self, start_calc, a, b, result):
        assert result == start_calc.mul(a, b)

    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name="add")
    @pytest.mark.parametrize('a,b,result', data['add1'],
                             ids=["int", "float", "bignum", "minus", "float+int"])
    def check_add(self, start_calc, a, b, result):
        assert result == start_calc.add(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,result', data['div1'],
                             ids=["int", "float", "bignum", "minus", "float+int"])
    @pytest.mark.dependency(depends=["mul"])
    def check_div(self, start_calc, a, b, result):
        try:
            assert result == start_calc.div(a, b)
        except Exception:
            raise Exception("除数不能为0")
