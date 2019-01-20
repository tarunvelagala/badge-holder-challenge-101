import pandas as pd
from keras.layers import *
from keras.models import *
from keras.utils.np_utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


classes = 2
batch_size = 2
input_shape = (9,)
df = pd.read_csv('csv/cancer.csv')
df = df.replace({'?': np.nan}).dropna()
test, train = train_test_split(df, test_size=0.8)

x_train, y_train = train.iloc[:, 0:9], train.iloc[:, 9]
x_test, y_test = test.iloc[:, 0:9], test.iloc[:, 9]
y_train = to_categorical(y_train, classes)
y_test = to_categorical(y_test, classes)
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=input_shape))
model.add(Dropout(.2))
model.add(Dense(classes, activation='softmax'))
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=50,
          verbose=1,
          validation_data=(x_test, y_test))
inputs = np.array([[3, 10, 7, 8, 5, 8, 7, 4, 1]])
prediction = model.predict(inputs)
print(prediction)
scores = model.evaluate(x_test, y_test)
print('The model prediction score is', scores)
# print(model.score(x_test, y_test))

