# -*- coding: utf-8 -*-
"""DeepLearning1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ukR_fvL7zFt-5Rjzhxmlc9enESDwOj5Y
"""



"""# **Load Data**"""

import tensorflow as tf
import matplotlib.pyplot as plt

# get the data and split it to training and test datasets
(train_images, train_labels), (test_images, test_labels)= tf.keras.datasets.mnist.load_data()

# scale down the values of the pixels from 0-255 to 0-1
train_images = train_images / 255.0
test_images = test_images / 255.0

# visualize the data
print(train_images.shape)
print(test_images.shape)
print(train_labels)

# display the first image
plt.imshow(train_images[0], cmap='gray')
plt.show()

# define the neural network
my_model = tf.keras.models.Sequential()
my_model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
my_model.add(tf.keras.layers.Dense(128, activation='relu'))
my_model.add(tf.keras.layers.Dense(10, activation='softmax'))

# compile the model
my_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# train my model
my_model.fit(train_images, train_labels, epochs=3)

# check the model accuracy on the test data
val_loss, val_acc = my_model.evaluate(test_images, test_labels)
print('Test accuracy: ', val_acc)

# save the model
my_model.save('my_mnist_model.h5')

# load the model from the file system
my_new_model = tf.keras.models.load_model('my_mnist_model.h5')

# check the new model for accuracy on the test data
new_val_loss, new_val_acc, = my_new_model.evaluate(test_images, test_labels)
print('New Test accuracy: ', new_val_acc)