#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from datetime import datetime, timedelta
from random import shuffle

def read_period_file(file):
    """ Opens the .txt file of the period calendar app. This function is meant 
    for the app Period Tracker of Simple Design Ltd."""
    period_cal = []
    periods = []

    # read the text file to a list as start-end pairs with datetime
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            newline = line.split("\t")
            if line.strip().split("\t")[1] == "Period Starts":
                period_cal.append([])
                # add start of period
                period_cal[-1].append(datetime.strptime(newline[0], "%d %b, %Y"))

            elif line.strip().split("\t")[1] == "Period Ends":
                # add end of period
                period_cal[-1].append(datetime.strptime(newline[0], "%d %b, %Y"))

    # make list of cycle and menstruation times
    for period in period_cal[1:]:
        num = period_cal.index(period)
        if num > 0:
            lengths = []
            # add first day
            lengths.append(period_cal[num][0])
            # add length of cycle
            lengths.append((period_cal[num][0] - period_cal[num - 1][0]).days)
            # add length of menstruation
            lengths.append((period_cal[num][1] - period_cal[num][0]).days + 1)

            periods.append(lengths)

    return periods


def make_train_test_sets(periods):
    """ Split into training and test sets, augment the data. """

    x = []
    y = []

    for period in periods[:-3]:
        p_index = periods.index(period)
        x.append([])
        x[-1].append([period[-2], period[-1]])
        x[-1].append([periods[p_index + 1][-2], periods[p_index + 1][-1]])
        x[-1].append([periods[p_index + 2][-2], periods[p_index + 2][-1]])
        y.append([periods[p_index + 3][-2], periods[p_index + 3][-1]])

    assert len(x) == len(y)

    x = x * 5
    y = y * 5
    train_size = int(len(y) * 0.8)
    
    train_x = np.array(x[0:train_size])
    train_y = np.array(y[0:train_size])

    test_x = np.array(x[train_size : len(x)])
    test_y = np.array(y[train_size : len(y)])
    
    # the last period of the train set, so that we can print a date on the 
    # predicted periods of the test set
    last_known_period = (periods*5)[train_size][0]

    return train_x, train_y, test_x, test_y, last_known_period


def load_synthetic_data(file):
    """ Split into training and test sets, augment the data. """
    
    periods = []
    with open(file, 'r') as f:
        for line in f:
            periods.append([int(x) for x in line.strip().split('\t')])

    x = []
    y = []

    for period in periods[:-3]:
        p_index = periods.index(period)
        x.append([])
        x[-1].append([period[-2], period[-1]])
        x[-1].append([periods[p_index + 1][-2], periods[p_index + 1][-1]])
        x[-1].append([periods[p_index + 2][-2], periods[p_index + 2][-1]])
        y.append([periods[p_index + 3][-2], periods[p_index + 3][-1]])

    assert len(x) == len(y)

    x = x * 5
    y = y * 5

    train_size = int(len(y) * 0.8)

    train_x = np.array(x[0:train_size])
    train_y = np.array(y[0:train_size])

    test_x = np.array(x[train_size : len(x)])
    test_y = np.array(y[train_size : len(y)])

    return train_x, train_y, test_x, test_y


def evaluate_predictions(test_y, predictions):
    """ Evaluate on the test set. """
    assert len(test_y) == len(predictions)

    right_cycle = 0
    right_menstr = 0

    for idx, y in enumerate(test_y):
        if y[0] == predictions[idx][0]:
            right_cycle += 1
        if y[1] == predictions[idx][1]:
            right_menstr += 1

    return right_cycle / len(test_y), right_menstr / len(test_y)


def print_predictions(last_known_period, predictions):
    
    # add the first predicted period
    next_periods = [[
        last_known_period + timedelta(days = predictions[0][0]),
        last_known_period + timedelta(days = predictions[0][0] + predictions[0][1]),
        predictions[0][1]
        ]]
    
    # add the next ones
    for period in predictions[1:]:
        last_period = next_periods[-1]
        next_periods.append([
            last_period[0] + timedelta(days = period[0]),
            last_period[0] + timedelta(days = period[0] + period[1]),
            period[1]
            ])
    
    for num, period in enumerate(next_periods):
        print(str(num) + ". From " + period[0].strftime('%d.%m.%Y') + \
              " to " + period[1].strftime('%d.%m.%Y') + ", length: " + str(period[2]))
    
    return next_periods
