import tensorflow as tf
import numpy as np

model = 'PrunedResnet_quant.tflite' # path to tflite file
start = 8 # first weight tensor index
stop = 17 # last weight tensor index + 1

interpreter = tf.lite.Interpreter(model_path=model)
interpreter.allocate_tensors()

tensors = []
for i in range(start, stop):
  x = np.array(interpreter.tensor(i)())
  x = np.rollaxis(x, 3, 1)
  tensors.append(x)
  
for tensor in tensors:
  print(tensor[0][0][0])

