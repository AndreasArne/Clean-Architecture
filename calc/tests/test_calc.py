#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_calc
----------------------------------

Tests for `calc` module.
"""

import pytest


from calc.calc import Calc


@pytest.fixture
def calculator():
    return Calc()

def test_add_two_numbers(calculator):
    res = calculator.add(4, 5)
    assert res == 9

def test_add_two_negative_numbers(calculator):
    res = calculator.add(-4, -5)
    assert res == -9
def test_add_one_negative_number(calculator):
    res = calculator.add(4, -5)
    assert res == -1
def test_add_one_negative_number_other(calculator):
    res = calculator.add(-4, 5)
    assert res == 1
def test_add_three_numbers(calculator):
    res = calculator.add(4, 5, 6)
    assert res == 15

def test_add_many_numbers(calculator):
    numbers = range(100)
    res = calculator.add(*numbers)
    assert res == 4950

def test_sub_to_numbers(calculator):
    res = calculator.sub(10, 3)
    assert res == 7

def test_mult_two_numbers(calculator):
    res = calculator.mult(6, 4)
    assert res == 24

def test_mult_many_numbers(calculator):
    s = range(1, 10)
    res = calculator.mult(*s)
    assert res == 362880

def test_mult_by_zero_raise_except(calculator):
    with pytest.raises(ValueError):
        calculator.mult(3, 0)
        

def test_div_two_numbers(calculator):
    res = calculator.div(13, 2)
    assert res == 6.5

def test_div_by_zero_returns_inf(calculator):
    res = calculator.div(13, 0)
    assert res == "inf"


def test_avg_correct_average(calculator):
    res = calculator.avg([2, 5, 12, 98])
    assert res == 29.25

def test_avg_removes_upper_outliers(calculator):
    res = calculator.avg([2, 5, 12, 98], ut=90)
    assert res == pytest.approx(6.333333)

def test_avg_removes_upper_outliers(calculator):
    res = calculator.avg([2, 5, 12, 98], lt=10)
    assert res == pytest.approx(55)

def test_avg_removes_upper_included(calculator):
    res = calculator.avg([2, 5, 12, 98], ut=98)
    assert res == 29.25
def test_avg_removes_lower_included(calculator):
    res = calculator.avg([2, 5, 12, 98], lt=2)
    assert res == 29.25
def test_avg_empty_list(calculator):
    res = calculator.avg([])
    assert res == 0
def test_avg_empty_list_after_outlier_removal(calculator):
    res = calculator.avg([12, 98], lt=15, ut=90)
    assert res == 0
def test_avg_empty_list_before_outlier_removal(calculator):
    res = calculator.avg([], lt=15, ut=90)
    assert res == 0
@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
