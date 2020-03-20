#!/usr/bin/env python
# coding: utf-8

# ##### Copyright 2019 The TensorFlow Authors.

# In[ ]:


#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# # TensorFlow 2 quickstart for beginners

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://www.tensorflow.org/tutorials/quickstart/beginner"><img src="https://www.tensorflow.org/images/tf_logo_32px.png" />View on TensorFlow.org</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />Run in Google Colab</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://github.com/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb"><img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />View source on GitHub</a>
#   </td>
#   <td>
#     <a href="https://storage.googleapis.com/tensorflow_docs/docs/site/en/tutorials/quickstart/beginner.ipynb"><img src="https://www.tensorflow.org/images/download_logo_32px.png" />Download notebook</a>
#   </td>
# </table>

# This short introduction uses [Keras](https://www.tensorflow.org/guide/keras/overview) to:
#
# 1. Build a neural network that classifies images.
# 2. Train this neural network.
# 3. And, finally, evaluate the accuracy of the model.

# This is a [Google Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb) notebook file. Python programs are run directly in the browser—a great way to learn and use TensorFlow. To follow this tutorial, run the notebook in Google Colab by clicking the button at the top of this page.
#
# 1. In Colab, connect to a Python runtime: At the top-right of the menu bar, select *CONNECT*.
# 2. Run all the notebook code cells: Select *Runtime* > *Run all*.

# Download and install TensorFlow 2. Import TensorFlow into your program:
#
# Note: Upgrade `pip` to install the TensorFlow 2 package. See the [install guide](https://www.tensorflow.org/install) for details.

# In[1]:

from __future__ import absolute_import, division, print_function, unicode_literals
import os, sys, traceback
print ("Check to make sure we are in the correct virtual environment:")

try:
    print (sys.real_prefix)
except:
    print ("Please run in a virtual environment")
    sys.exit()

for py in sys.path:
    if "python3" in py:
        print(py)
        break
if "anaconda" in py:
    print ("Anaconda should be overridden with a virtualenv called 'venv'")
    sys.exit()

if "venv" not in py:
    print ("Please use the convention that your virtualenv is called 'venv'")
    sys.exit()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"             #reduce tf's blabbering to a dull roar

import tensorflow as tf
print ("Tensorflow version:", tf.version.VERSION)
try:
    print ("Test for gpu:", tf.test.is_gpu_available())
except:
    traceback.print_exc()
    print ("GPU is installed but something is wrong. Possibly another tensorflow session is active, for instance if you are running a Jupyter kernel on this machine")
    sys.exit()

# Load and prepare the [MNIST dataset](http://yann.lecun.com/exdb/mnist/). Convert the samples from integers to floating-point numbers:

# In[ ]:


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


# Build the `tf.keras.Sequential` model by stacking layers. Choose an optimizer and loss function for training:

# In[ ]:


model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])


# For each example the model returns a vector of "[logits](https://developers.google.com/machine-learning/glossary#logits)" or "[log-odds](https://developers.google.com/machine-learning/glossary#log-odds)" scores, one for each class.

# In[ ]:


predictions = model(x_train[:1]).numpy()
predictions


# The `tf.nn.softmax` function converts these logits to "probabilities" for each class:

# In[ ]:


tf.nn.softmax(predictions).numpy()


# Note: It is possible to bake this `tf.nn.softmax` in as the activation function for the last layer of the network. While this can make the model output more directly interpretable, this approach is discouraged as it's impossible to
# provide an exact and numerically stable loss calculation for all models when using a softmax output.

# The `losses.SparseCategoricalCrossentropy` loss takes a vector of logits and a `True` index and returns a scalar loss for each example.

# In[ ]:


loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)


# This loss is equal to the negative log probability of the the true class:
# It is zero if the model is sure of the correct class.
#
# This untrained model gives probabilities close to random (1/10 for each class), so the initial loss should be close to `-tf.log(1/10) ~= 2.3`.

# In[ ]:


loss_fn(y_train[:1], predictions).numpy()


# In[ ]:


model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])


# The `Model.fit` method adjusts the model parameters to minimize the loss:

# In[ ]:


model.fit(x_train, y_train, epochs=5)


# The `Model.evaluate` method checks the models performance, usually on a "[Validation-set](https://developers.google.com/machine-learning/glossary#validation-set)".

# In[ ]:


model.evaluate(x_test,  y_test, verbose=2)


# The image classifier is now trained to ~98% accuracy on this dataset. To learn more, read the [TensorFlow tutorials](https://www.tensorflow.org/tutorials/).

# If you want your model to return a probability, you can wrap the trained model, and attach the softmax to it:

# In[ ]:


probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])


# In[ ]:


probability_model(x_test[:5])


# In[ ]:


os.system('which pip')


# In[2]:


tf


# In[3]:


tf.version.VERSION


# In[ ]:
