#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task02 module"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Shoplist cost per item"""
    res = {}

    for k, v in shoplist.iteritems():
        try:
            cost = float(FRUIT[k])
            res[k] = cost*float(v)
        except:
            pass
    return res


def get_total_cost(shoplist):
    """Shoplist total cost of items"""
    cost_per_item = get_cost_per_item(shoplist)
    sum = 0
    for k, v in cost_per_item.iteritems():
        sum = sum + float(v)
        return sum
