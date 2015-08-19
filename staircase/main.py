#!/usr/bin/env python
# -*- coding: utf-8 -*-

N = int(raw_input())
for i in xrange(N):
    num = i + 1
    width = N
    print(' ' * (width - num) + '#' * num)