#Install all the relevant packages to Build the model for this Regression Problem
# Predict the area using Keras Regression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras import Sequential
from keras.layers import Dense
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.wrappers.scikit_learn import KerasRegressor

data = pd.read_csv("C:/Users/personal/Desktop/fireforests.csv")

data = data.iloc[:,2:29]

data.info()

# All the variableas are numeric so no need to categorise the data

def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)

data_n = norm_func(data.iloc[:,:])

# Rearrange the columns

data_n = data_n.iloc[:,[8,0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]]

# Build the ANN Model for the FF Normalised Data Set

x = data_n.iloc[:,1:27]
y = data_n.iloc[:,0]
y = np.array(y)
y = np.reshape(y,(-1,1))
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()
print(scaler_x.fit(x))
xscale = scaler_x.transform(x)
print(scaler_y.fit(y))
yscale = scaler_y.transform(y)

X_train, X_test, y_train, y_test = train_test_split(xscale, yscale)

model = Sequential()
model.add(Dense(12, input_dim=26, kernel_initializer='normal', activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))
model.summary()

model.compile(loss='mse', optimizer='adam', metrics=['mse','mae'])
history = model.fit(X_train, y_train, epochs=40, batch_size=50,  verbose=1, validation_split=0.2)

print(history.history.keys())
import matplotlib.pyplot as plt
# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()



