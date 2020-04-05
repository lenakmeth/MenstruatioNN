# MenstruatioNN

A simple LSTM model, to predict menstrual cycles and length of menstruation. Powered by Keras.

## Requirements

- Python3
- Keras


## Data
I use the log file of the app [Period Tracker](https://play.google.com/store/apps/details?id=com.popularapp.periodcalendar&hl=en). For privacy reasons, I am not going to share my personal data, but I am happy to make a read function for the log file of a different app, if you provide me the format. The format of this log file is:

> D1 M1, 20YY	Period Starts
D2 M1, 20YY	Period Ends
D3 M2, 20YY	Period Starts
D4 M2, 20YY	Period Ends

## Results

|                                   	| LSTM 	| 
|-----------------------------------	|-------|
| Train set                         	| 284   | 
| Test set                          	| 71 	|
| Epochs	                         	| 4000	|
| Accuracy (menstrual cycle length) 	| 0.9859|
| Accuracy (menstruation length)    	| 0.9718|

## References

Brownlee, Jason. “Multi-Step Time Series Forecasting with Long Short-Term Memory Networks in Python,” August 5, 2019. https://machinelearningmastery.com/multi-step-time-series-forecasting-long-short-term-memory-networks-python/.