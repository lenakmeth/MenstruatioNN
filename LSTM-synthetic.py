#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import *
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras import metrics
from keras.models import load_model
import numpy as np

# Load datasets

# Load synthetic data
train_x, train_y, _, _ = load_synthetic_data("synthetic_data.txt")

# Load real data
periods = read_period_file("calendar.txt")
train_x_, train_y_, test_x, test_y, last_known_period = make_train_test_sets(periods)

# Append real data to synthetic data
train_x = np.array(train_x.tolist() + train_x_.tolist()[-78:])
train_y = np.array(train_y.tolist() + train_y_.tolist()[-78:])


train = True
n_epochs = 4000

if train:
    # Configuration
    n_steps = 3
    n_features = train_x.shape[2]
    
    # LSTM model
    model = Sequential()
    model.add(LSTM(100, activation="relu", 
                   return_sequences=True, 
                   input_shape=(n_steps, n_features)))
    model.add(LSTM(100, activation="relu"))
    model.add(Dense(n_features))
    model.compile(optimizer="adam", 
                  loss="mse", 
                  metrics=[metrics.mae, metrics.mape])
    
    # fit model
    model.fit(train_x, train_y, 
              epochs=n_epochs, 
              verbose=2, 
              #validation_data=(test_x, test_y)
              )
    
    model.evaluate(test_x, test_y)
    
    # Serialize model to HDF5
    model.save("lstm_" + str(n_epochs) + ".h5")
    print("Saved model to disk")

else:
    # Load model if saved
    model = load_model("lstm_" + str(n_epochs) + ".h5")
    model.summary()

# Make predictions
y_preds = model.predict(test_x, verbose=0)
predictions = [[int(round(i[0])), int(round(i[1]))] for i in y_preds]
accuracies = evaluate_predictions(test_y, predictions)

print("Accuracy of menstrual cycle length prediction: ", round(accuracies[0], 4))
print("Accuracy of menstruation length prediction: ", round(accuracies[1], 4))
# print("Next periods: ")
# next_periods = print_predictions(last_known_period, predictions)

print(len(train_y))
print(len(test_y))