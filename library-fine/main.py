#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Date, Month, Year
returned = map(int, raw_input().split(' '))
expected = map(int, raw_input().split(' '))

if expected[2] < returned[2]:
    # year penalty
    fine = 10000
elif (expected[2] == returned[2] and
        expected[1] < returned[1]):
    fine = 500 * (returned[1] - expected[1])
elif (expected[2] == returned[2] and
        expected[1] == returned[1] and
        expected[0] < returned[0]):
    fine = 15 * (returned[0] - expected[0])
else:
    fine = 0

print fine