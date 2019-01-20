# cancer_prediction

```
pip install tensorflow keras numpy pandas scikit-learn
```
This model is based on prediction of **Benign** or **Malignancy**

**_python keras_cancer.py_**
#### Output => keras_cancer.py, epochs=50

```
Epoch 46/50
546/546 [==============================] - 0s 848us/step - loss: 0.0476 - acc: 0.9835 - val_loss: 0.1169 - val_acc: 0.9632
Epoch 47/50
546/546 [==============================] - 0s 873us/step - loss: 0.0524 - acc: 0.9780 - val_loss: 0.1157 - val_acc: 0.9632
Epoch 48/50
546/546 [==============================] - 0s 835us/step - loss: 0.0417 - acc: 0.9872 - val_loss: 0.1014 - val_acc: 0.9779
Epoch 49/50
546/546 [==============================] - 0s 851us/step - loss: 0.0414 - acc: 0.9890 - val_loss: 0.1418 - val_acc: 0.9632
Epoch 50/50
546/546 [==============================] - 0s 876us/step - loss: 0.0514 - acc: 0.9762 - val_loss: 0.1055 - val_acc: 0.9632
[[4.5144334e-04 9.9954849e-01]]
136/136 [==============================] - 0s 25us/step
The model prediction score is [0.10546428061035626, 0.9632352941176471]
```
\
\
\
**_python random_forest_cancer.py_**
This model is based on prediction of **Benign** or **Malignancy**
#### Output => random_forest_cancer.py
```
diagnosis
B    357
M    212
dtype: int64
Accuracy is:  0.9707602339181286
[[107   1]
 [  4  59]]
 ```
\
\
\
**_python mammogram.py_**
\
This model is based on the elementary features like **"BI_RADS", "age", "shape", "margin", "density", "severity"**
#### Output => mammogram.py
```
[[ 0.3211177   0.7650629   0.17563638  1.39618483  0.24046607]
 [ 0.3211177   0.15127063  0.98104077  1.39618483  0.24046607]
 [-0.20875843 -1.89470363 -1.43517241 -1.157718    0.24046607]
 ...
 [-0.20875843  0.56046548  0.98104077  1.39618483  0.24046607]
 [ 0.3211177   0.69686376  0.98104077  1.39618483  0.24046607]
 [-0.20875843  0.42406719  0.17563638  0.11923341  0.24046607]]
Accuracy is  0.8317307692307693
```

