#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import *
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras import metrics
from keras.models import load_model

# Load datasets
periods = read_period_file("calendar.txt")
train_x, train_y, test_x, test_y, last_known_period = make_train_test_sets(periods)
train = True

if train:
    # Configuration
    n_steps = 3
    n_epochs = 4000
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

# Load model if saved
model = load_model("lstm_4000.h5")
model.summary()

# Make predictions
y_preds = model.predict(test_x, verbose=0)
predictions = [[int(round(i[0])), int(round(i[1]))] for i in y_preds]
accuracies = evaluate_predictions(test_y, predictions)

print("Accuracy of menstrual cycle length prediction: ", accuracies[0])
print("Accuracy of menstruation length prediction: ", accuracies[1])
print("Next periods: ")
next_periods = print_predictions(last_known_period, predictions)
