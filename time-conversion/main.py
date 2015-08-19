#!/usr/bin/env python
# -*- coding: utf-8 -*-

timestamp = raw_input()
hh = int(timestamp[:2])
mm = timestamp[3:5]
ss = timestamp[6:8]
apm = timestamp[8:10]

#print(hh, mm, ss, apm)
if hh != 12 and apm == 'PM':
    hh += 12
elif hh == 12 and apm == 'AM':
    hh -= 12
print('{0}:{1}:{2}'.format(str(hh).zfill(2), mm, ss))