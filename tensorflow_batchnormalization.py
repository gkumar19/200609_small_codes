# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:03:10 2020

Understanding batch normalization layers:
each neuron is attached to one neuron of batchnormalisation layer independently having 2 or 3 or 4 parameters
2 in case of no learnable parameters and only storing mean and std
4 in case of learnable parameters in to stretch the inputs

@author: KGU2BAN
"""

import numpt as np
from tensorflow.keras.layers import BatchNormalization, Dense
import tensorflow as tf
means = [1, 2, 3, 4]
stds = [9, 8, 7, 6]
xi = [np.random.randn(5000, 1)* std + mean for std, mean in zip(stds, means)]
x = np.concatenate(xi, axis=1)

model = tf.keras.models.Sequential([BatchNormalization(epsilon = 0, name='batchnorm1', center=False, scale=False, input_shape=(4,)),
                                    Dense(1, name='dense1')]) 

model.compile('adam', 'mse')

model.fit(x,np.random.randn(5000, 1), epochs=10000, batch_size=5000)
model.summary()

model_function = tf.keras.backend.function(model.input, model.get_layer('batchnorm1').output)

weights = model.get_layer(name='batchnorm1').get_weights() # These weights should have stored above means and stds

tranformation = model_function(np.array([[0,0,0,0]])) # These are equal to (0-weights[0][0])/np.sqrt(weights[1][0])
