#!/usr/bin/env python
# -*- coding: utf-8 -*-

N = int(raw_input())
fact = 1
for i in xrange(N, 1, -1):
    fact *= i
print(fact)