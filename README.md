# MenstruatioNN

A simple LSTM model, to predict menstrual cycles and length of menstruation. Powered by Keras.

## Requirements

- Python3
- Keras


## Data
I use the log file of the app [Period Tracker](https://play.google.com/store/apps/details?id=com.popularapp.periodcalendar&hl=en). For privacy reasons, I am not going to share my personal data, but I am happy to make a read function for the log file of a different app, if you provide me the format. The format of this log file is:

> D1 M1, 20YY	Period Starts
> D2 M1, 20YY	Period Ends
> D3 M2, 20YY	Period Starts
> D4 M2, 20YY	Period Ends

There is also a file with synthetic data, which is used ofr training. 

## Results

|                                 |                |               |        |  Accuracy pred.  |    Accuracy pred.   |
|            Train set            | Train set size | Test set size | Epochs | mensturation day | menstruation length |
|:-------------------------------:|:--------------:|:-------------:|:------:|:----------------:|:-------------------:|
|   Real data (no augmentation)   |       78       |       20      |  4000  |       0.25       |         0.45        |
|          Real data (x5)         |       392      |       98      |  4000  |       **0.98**       |         **0.96**        |
|     Real data (x5) shuffled     |       392      |       98      |  4000  |       0.20       |         0.46        |
|          Synthetic data         |      1988      |       98      |  4000  |       0.14       |         0.38        |
|    Synthetic data + Real data   |      2066      |       98      |  4000  |       0.67       |         0.86        |
| Synthetic data + Real data (x5) |      2380      |       98      |  4000  |       **0.98**       |         **0.96**        |

## References

Brownlee, Jason. “Multi-Step Time Series Forecasting with Long Short-Term Memory Networks in Python,” August 5, 2019. https://machinelearningmastery.com/multi-step-time-series-forecasting-long-short-term-memory-networks-python/.
