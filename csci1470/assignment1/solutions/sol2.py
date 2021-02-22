import sys
import numpy as np
import gzip

train_size = 10000
test_size = 10000
image_size = 784
learning_rate = 0.5

def import_images(filepath, num_images=10000, offset=16):
	with open(filepath, "rb") as f, gzip.GzipFile(fileobj=f) as bytestream:
		dt = np.dtype(np.uint8).newbyteorder(">")
		images = np.frombuffer(bytestream.read(num_images * image_size + offset), dtype=dt, offset=offset) / 255.0
		return images.reshape((num_images, image_size))

def import_labels(filepath, num_labels=10000, offset=8):
	with open(filepath, "rb") as f, gzip.GzipFile(fileobj=f) as bytestream:
		dt = np.dtype(np.uint8).newbyteorder(">")
		return np.frombuffer(bytestream.read(num_labels + offset), dtype=dt, offset=offset)

def softmax(vector):
	max_logit = np.amax(vector) 
	exp_vector = [np.exp(logit - max_logit) for logit in vector] 
	return exp_vector / sum(exp_vector) 

def forward_pass(image):
	result = image.dot(weights) + bias # (10,)
	softmax_vector = softmax(result)
	return softmax_vector

def backward_pass(image, softmax_vector, label):
	delta_bias = np.array([((1 if i == label else 0) - softmax_vector[i]) * learning_rate 
		for i in range(len(softmax_vector))])
	gradient = (delta_bias / learning_rate) * -1
	delta_weights = -learning_rate * np.outer(image, gradient)
	return delta_weights, delta_bias

def predict(image):
	return np.argmax(image.dot(weights) + bias)

def train_model(weights, bias, train_images, train_labels):
	for i in range(len(train_images)):
		softmax_vector = forward_pass(train_images[i])
		delta_weights, delta_bias = backward_pass(train_images[i],
			softmax_vector, train_labels[i])
		weights += delta_weights
		bias += delta_bias

def test_model(weights, bias, test_images, test_labels):
	predictions = np.array([1.0 if predict(test_images[i]) == test_labels[i] else 0 for i in range(len(test_images))])
	print(sum(predictions) / len(predictions))

# python mnist.py train-images-idx3-ubyte.gz train-labels-idx1-ubyte.gz t10k-images-idx3-ubyte.gz t10k-labels-idx1-ubyte.gz
if __name__ == '__main__':

	train_images = import_images('./train-images-idx3-ubyte.gz')
	train_labels = import_labels('./train-labels-idx1-ubyte.gz')
	test_images = import_images('./t10k-images-idx3-ubyte.gz')
	test_labels = import_labels('./t10k-labels-idx1-ubyte.gz')

	weights = np.zeros((784, 10))
	bias = np.zeros(10)

	train_model(weights, bias, train_images, train_labels)
	test_model(weights, bias, test_images, test_labels)