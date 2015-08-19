#!/usr/bin/env python
# -*- coding: utf-8 -*-

def run_test(N):
    n_5, n_3 = 0, 0
    while N > 0:
        if (N - 3) >= 8:
            n_5 += 3
            N -= 3
        elif N == 11:
            n_5 += 6
            n_3 += 5
            N = 0
        elif N == 10:
            n_3 += 10
            N = 0
        elif N == 9:
            n_5 += 9
            N = 0
        elif N == 8:
            n_5 += 3
            n_3 += 5
            N = 0
        elif N % 3 == 0:
            n_5 += N
            N = 0
        elif N % 5 == 0:
            n_3 += N
            N = 0
        else:
            return '-1'
    return '5' * n_5 + '3' * n_3


n_test = int(raw_input())

for _ in xrange(n_test):
    N = int(raw_input())
    decent_num = run_test(N)
    if decent_num == '':
        decent_num = '-1'
    print(decent_num)
