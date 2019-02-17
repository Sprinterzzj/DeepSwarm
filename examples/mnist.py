# Copyright (c) 2019 Edvinas Byla
# Licensed under MIT License

import context
import tensorflow as tf

from deepswarm.backends import Dataset, TFKerasBackend
from deepswarm.deepswarm import DeepSwarm

# Load MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Normalize and reshape data
x_train, x_test = x_train / 255.0, x_test / 255.0
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = x_train.shape[1:]
# Create dataset object, which controls all the data
normalized_dataset = Dataset(
    training_examples=x_train,
    training_labels=y_train,
    testing_examples=x_test,
    testing_labels=y_test,
    validation_split=0.1,
)
# Create backend responsible for training & validating
backend = TFKerasBackend(
    dataset=normalized_dataset,
    input_shape=input_shape,
    output_size=10
)
# Create DeepSwarm object responsible for optimization
deepswarm = DeepSwarm(backend=backend)
deepswarm.find_topology(max_depth=2, swarm_size=2)
