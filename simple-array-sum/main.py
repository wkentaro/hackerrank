#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.hackerrank.com/challenges/simple-array-sum

N = int(raw_input())
nums = map(int, raw_input().split(' '))

assert N == len(nums)
print(sum(nums))