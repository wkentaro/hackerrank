#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from math import sqrt, acos, pi

length_AB = int(raw_input())
length_BC = int(raw_input())

a = length_AB
b = length_BC

length_CM = sqrt(a**2 + b**2) / 2
c = length_CM

length_BM = sqrt(1/2 * (a**2 + b**2) - c**2)
d = length_BM

cos_theta = (c**2 - b**2 - d**2) / (-2*b*d)
theta = acos(cos_theta) / pi * 180  # [deg]

print('{0}{1}'.format(int(round(theta)), '°'))