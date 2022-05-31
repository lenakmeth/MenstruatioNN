#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from utils import *
from random import choices, shuffle

periods = read_period_file("calendar.txt")
train_x, train_y, test_x, test_y, last_known_period = make_train_test_sets(periods)

men_days = [i[1] for i in periods]
men_blood = [i[2] for i in periods]

# Counter({27: 21, 29: 19, 28: 17, 30: 14, 32: 8, 26: 7, 31: 5, 25: 3, 33: 3, 24: 3, 23: 1})
# Counter({6: 55, 5: 37, 4: 4, 7: 3, 3: 1, 8: 1})

fake_days = [28]*100 + [27]*100 + [29]*100
fake_days += choices(range(23,36), k = 200)


fake_dur = [4]*100 + [5]*100 + [6]*100
fake_dur += choices(range(3,8), k = 200)

shuffle(fake_days)
shuffle(fake_dur)

# make
fake_periods = []
for num, x in enumerate(fake_days):
    fake_periods.append([x, fake_dur[num]])
    
with open('syntetic_data.txt', 'w') as f:
    for x in fake_periods:
        f.write(str(x[0]) + '\t' + str(x[1]) + '\n')