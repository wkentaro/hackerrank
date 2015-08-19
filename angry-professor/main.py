#!/usr/bin/env python
# -*- coding: utf-8 -*-

def run_test(n_student, n_limit, arrived_at):
    n_attend = 0
    for t in arrived_at:
        if t <= 0:
            n_attend += 1
    if n_attend < n_limit:
        print('YES')
    else:
        print('NO')


n_test = int(raw_input())
for _ in xrange(n_test):
    n_student, n_limit = map(int, raw_input().split(' '))
    arrived_at = map(int, raw_input().split(' '))
    run_test(n_student, n_limit, arrived_at)
