# -------------------------------------------------------------------------------
# Name:         pytest第一节直播课作业
# Description:
# Author:       zhangdonghui
# Date:         2020/6/26
# -------------------------------------------------------------------------------
from hogwartstest.calculator import *
import pytest
import yaml

data = yaml.safe_load(open("calculator_data.yml"))


class Testcal:
    @pytest.mark.add
    def test_add(self, start_calc):
        a1 = data['add1']
        assert a1['result'][0] == start_calc.add(a1['a'][0], a1['b'][0])
        assert a1['result'][1] == start_calc.add(a1['a'][1], a1['b'][1])
        assert a1['result'][2] == start_calc.add(a1['a'][2], a1['b'][2])
        assert a1['result'][3] == start_calc.add(a1['a'][3], a1['b'][3])
        assert a1['result'][4] == start_calc.add(a1['a'][4], a1['b'][4])

    @pytest.mark.minus
    def test_minus(self, start_calc):
        a2 = data['minus1']
        assert a2['result'][0] == start_calc.minus(a2['a'][0], a2['b'][0])
        assert a2['result'][1] == start_calc.minus(a2['a'][1], a2['b'][1])
        assert a2['result'][2] == start_calc.minus(a2['a'][2], a2['b'][2])
        assert a2['result'][3] == start_calc.minus(a2['a'][3], a2['b'][3])
        assert a2['result'][4] == start_calc.minus(a2['a'][4], a2['b'][4])

    @pytest.mark.mul
    def test_mul(self, start_calc):
        a3 = data['mul1']
        assert a3['result'][0] == start_calc.mul(a3['a'][0], a3['b'][0])
        assert a3['result'][1] == start_calc.mul(a3['a'][1], a3['b'][1])
        assert a3['result'][2] == start_calc.mul(a3['a'][2], a3['b'][2])
        assert a3['result'][3] == start_calc.mul(a3['a'][3], a3['b'][3])
        assert a3['result'][4] == start_calc.mul(a3['a'][4], a3['b'][4])

    @pytest.mark.div
    def test_div(self, start_calc):
        a4 = data['div1']
        assert a4['result'][0] == start_calc.div(a4['a'][0], a4['b'][0])
        assert a4['result'][1] == start_calc.div(a4['a'][1], a4['b'][1])
        assert a4['result'][2] == start_calc.div(a4['a'][2], a4['b'][2])
        assert a4['result'][3] == start_calc.div(a4['a'][3], a4['b'][3])
        assert a4['result'][4] == start_calc.div(a4['a'][4], a4['b'][4])
