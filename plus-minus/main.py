#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_input():
    N = int(raw_input())
    nums = map(int, raw_input().split(' '))
    return N, nums

def put_in_order_with_sign(lst):
    positive, zeros, negative = [], [], []
    for el in lst:
        if el > 0:
            positive.append(el)
        elif el == 0:
            zeros.append(el)
        else:
            negative.append(el)
    return positive, zeros, negative

N, nums = get_input()
pos, zeros, neg = put_in_order_with_sign(nums)
fractions = map(lambda x: 1.*x/N, [len(pos), len(neg), len(zeros)])
for fr in fractions:
    print(fr)
