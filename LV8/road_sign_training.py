from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing import image_dataset_from_directory

from matplotlib import pyplot as plt
import numpy as np

train_ds = image_dataset_from_directory(
 directory='archive/Train/',
 labels='inferred',
 label_mode='categorical',
 batch_size=32,
 image_size=(48, 48))

test_ds = image_dataset_from_directory(
 directory='archive/Test_dir/',
 labels='inferred',
 label_mode='categorical',
 batch_size=1,
 image_size=(48, 48))

inputs = keras.Input(shape=(48,48,3))
x = layers.experimental.preprocessing.Rescaling(1./255)(inputs)
x = layers.Conv2D(32,kernel_size=(3,3), padding='same', activation="relu")(x)
x = layers.Conv2D(32,kernel_size=(3,3), padding='valid', activation="relu")(x)
x = layers.MaxPool2D(pool_size=(2,2), strides=(2,2))(x)
x = layers.Dropout(rate= 0.2)(x)
x = layers.Conv2D(64, kernel_size=(3,3), padding="same", activation="relu")(x)
x = layers.Conv2D(64, kernel_size=(3,3), padding="valid", activation="relu")(x)
x = layers.MaxPool2D(pool_size=(2,2), strides=(2,2))(x)
x = layers.Dropout(rate= 0.2)(x)
x = layers.Conv2D(128, kernel_size=(3,3), padding="same", activation="relu")(x)
x = layers.Conv2D(128, kernel_size=(3,3), padding="valid", activation="relu")(x)
x = layers.MaxPool2D(pool_size=(2,2), strides=(2,2))(x)
x = layers.Dropout(rate= 0.2)(x)
x = layers.Flatten()(x)
x = layers.Dense(512, activation="relu")(x)
x = layers.Dropout(rate = 0.5)(x)
outputs = layers.Dense(43, activation="softmax")(x)

model = keras.Model(inputs=inputs, outputs=outputs, name="gtsrb_model")
model.summary()

history = model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

epochs=2
history = model.fit(train_ds, epochs=epochs)

score = model.evaluate(test_ds)
print("Test loss: ", score[0])
print("Test accuracy: ", score[1])



