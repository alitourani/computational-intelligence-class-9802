
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import random

DATADIR = "PATH!"
CATEGORIES = []

# Defines category
for i in range(1, 7):
    CATEGORIES.append(str(i))

# Change the pictures size in 150px x 150px
IMG_SIZE = 150


training_data = []

def create_training_data():
    for category in CATEGORIES:  # do for each class
        path = os.path.join(DATADIR,category)  # create path to each class
        class_num = CATEGORIES.index(category) # get the class number
        for img in tqdm(os.listdir(path)):  # iterate over each image
            try:
                # convert to array(in Grayscale)
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)
                
                # we crop the the picture to get the face exactly
                img_array = cv2.resize(img_array, (128, 128) )
                img_array = img_array[5:115, 5:115]
                
                # resize to normalize data size
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  
                
                # add this to our training_data
                training_data.append([new_array, class_num])
                
             # in the interest in keeping the output clean...
            except Exception as e: 
                pass
        
create_training_data()
# Chane the position of Training_data to get the better performance
random.shuffle(training_data)

X = []
y = []

# fill the data and its label to X and y
for features,label in training_data:
    X.append(features)
    y.append(label)

# Change to numpy array with special reshape 
y = np.array(y)
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

# Feature scaling(using max-min)
X = X/255.0


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import MaxPooling2D 
from tensorflow.keras.layers import Dropout 

# If you install tensorflow gpu, use this to train data with your GPU 
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction = 0.333)
sess = tf.Session(config = tf.ConfigProto(gpu_options = gpu_options))


#Initializing the CNN
classifier=Sequential()

#S1 Convolution + Pooling
classifier.add(Conv2D(32, (3, 3), padding='same', input_shape=(150,150,1), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Conv2D(32, (3, 3), padding='same', activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

classifier.add(Conv2D(128, (3, 3), padding='same', activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

#S2 Flattening
classifier.add(Flatten())

#S3 Fully connected 
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dropout(0.5))
classifier.add(Dense(units=64, activation='relu'))
classifier.add(Dropout(0.5))
classifier.add(Dense(units=6, activation='softmax'))


#Compiling the CNN
classifier.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
classifier.fit(X, y, batch_size=32, epochs=60, validation_split=0.3)


## Save the model
#classifier.save('AgeDetectinM.model')

## Load the model
#from tensorflow import keras
#classifier = keras.models.load_model('AgeDetectinM.model')


# Test the model 
from PIL import Image
img = cv2.imread("PATH!" ,cv2.IMREAD_GRAYSCALE )
IMG_SIZE = 150
img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

# Show the picture
plt.imshow(f, cmap='gray')
plt.show()

#pridicte
pr = classifier.predict(np.array(f).reshape(-1, IMG_SIZE, IMG_SIZE, 1))
Result = (np.where(max(pr) == np.amax(max(pr))))[0][0] + 1

if Result == 1:
    print("Predicted Age is in range [0 to 5]")
elif Result == 2:
    print("Predicted Age is in range [6 to 16]")
elif Result == 3:
    print("Predicted Age is in range [17 to 30]")
elif Result == 4:
    print("Predicted Age is in range [31 to 50]")
elif Result == 5:
    print("Predicted Age is in range [51 to 80]")
else:
    print("Predicted Age is in range [81 to 100]")
    





