""" CSCI1470 Assignment 1

Response by Lucien Gaitskell

References:
- https://brown-deep-learning.github.io/dl-website-2020/projects/public/hw1-mnist-numpy/hw1-mnist-numpy.html
"""
import numpy as np
from pathlib import Path
import requests
import gzip
import os
import io
# Killing optional CPU driver warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
DEBUG = False

PACKAGE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(PACKAGE_DIR, "bin")


class DataFile:
    """ Represents data file configuration """
    def __init__(self, name, url):
        self.name = name
        self.url = url


class DataLoader:
    """ Handle remote and local loading of training and test data """
    TRAIN_IMAGE = DataFile("train_image", "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz")
    TRAIN_LABEL = DataFile("train_label", "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz")
    TEST_IMAGE = DataFile("test_image", "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz")
    TEST_LABEL = DataFile("test_label", "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz")

    def __init__(self):
        self.data_path = Path(DATA_DIR)

        # MNIST config:
        self.train_images = self._load_file(self.TRAIN_IMAGE, header=16, dsize=784, normalize=True)
        self.train_labels = self._load_file(self.TRAIN_LABEL, header=8, dsize=1)
        self.test_images = self._load_file(self.TEST_IMAGE, header=16, dsize=784, normalize=True)
        self.test_labels = self._load_file(self.TEST_LABEL, header=8, dsize=1)

    @staticmethod
    def _download(url):
        """ Download content from URL """
        r = requests.get(url)
        return r.content

    @staticmethod
    def _load_fdata(fstream, header, dsize, normalize=False):
        """
        Load file stream into list of numpy arrays based on characteristics

        Args:
            fstream: file stream to read from
            header: header length to ignore (bytes)
            dsize: size of each individual numpy array

        Returns: list of numpy arrays

        """
        with gzip.GzipFile(fileobj=fstream) as bytestream:
            data = np.frombuffer(bytestream.read(), np.uint8, offset=header)

        if normalize:
            data = data.astype(np.float64)
            data /= 255.0

        if dsize == 1:
            shape = -1
        else:
            shape = (-1, dsize)

        return data.reshape(shape)

    @classmethod
    def _load_file(cls, dfile: DataFile, header, dsize, **kwargs):
        """ Load given file, first from disk and fallback to remote. """
        disk_file = Path(DATA_DIR) / dfile.name     # Local path

        if not disk_file.exists():                  # Download if missing
            print("Download file: {}".format(dfile.name))
            with open(disk_file, 'wb') as f:
                f.write(cls._download(dfile.url))

        with open(disk_file, 'rb') as f:            # Load from file (must be present)
           return cls._load_fdata(f, header=header, dsize=dsize, **kwargs)


class Model:
    """
        This model class provides the data structures for your NN, 
        and has functions to test the three main aspects of the training.
        The data structures should not change after each step of training.
        You can add to the class, but do not change the 
        stencil provided except for the blanks and pass statements.
        Make sure that these functions work with a loop to call them multiple times,
        instead of implementing training over multiple steps in the function
        Arguments: 
        train_images - NumPy array of training images
        train_labels - NumPy array of labels
    """
    def __init__(self, train_images, train_labels):
        input_size, self.num_classes, self.batch_size, self.learning_rate = 784, 10, 100, 0.5
        self.train_images = train_images
        self.train_labels = train_labels
        # sets up weights and biases...

        # Weights are indexed by pixel then by class (number)
        self.W = np.zeros((input_size, self.num_classes,), dtype=np.float64)
        # Biases for each class (number)
        self.b = np.zeros((self.num_classes,), dtype=np.float64)

        self.current_start = 0

    def run(self):
        """
        Does the forward pass, loss calculation, and back propagation
        for this model for one step
        Args: None
        Return: None
        """
        self.run_batch(self.current_start, self.current_start+self.batch_size)
        self.current_start += self.batch_size

    def run_to(self, end=None):
        if DEBUG: print("Start train")

        if end is None:
            end = self.train_images.shape[0]

        for i in range(0, end, self.batch_size):
            self.run_batch(i, i+self.batch_size)

    def logits(self, data):
        logits_original = np.dot(data, self.W) + self.b
        """
        # will be in the format of:
        [
            [perceptron 1, perceptron 2, perceptron 3, ...],  # image 1
            [perceptron 1, perceptron 2, perceptron 3, ...],  # image 2
            [perceptron 1, perceptron 2, perceptron 3, ...],  # image 3
            ... 
        ]
        """
        if DEBUG: print("Original Logits:", logits_original.shape)
        return logits_original

    @staticmethod
    def softmax(logits_original):
        logits_power = np.exp(logits_original)
        logit_sums = np.sum(logits_power, axis=1).reshape((-1, 1))
        logits = logits_power / logit_sums
        # logits = - np.log(logits_softmax)

        return logits

    def one_hots(self, data_labels):
        one_hot_labels = np.eye(self.num_classes)[data_labels].reshape((-1, self.num_classes,))
        """
        # will be in the format of:
        [
            [perceptron 1, perceptron 2, perceptron 3, ...],  # image 1
            [perceptron 1, perceptron 2, perceptron 3, ...],  # image 2
            [perceptron 1, perceptron 2, perceptron 3, ...],  # image 3
            ... 
        ]
        where for each image only one perceptron is `1` and the others are `0`
        """
        if DEBUG: print("one_hot:", one_hot_labels.shape)

        return one_hot_labels

    def loss(self, one_hot_labels, logits):
        loss = one_hot_labels - logits
        # loss = -np.log(loss_delta)
        if DEBUG: print("loss: {} max, {} min, {} mean".format(loss.max(), loss.min(), np.mean(loss)))
        return loss

    def loss_adjustment(self, data, loss):
        return data @ loss

    def backprop(self, delta_W, delta_b):
        self.W += delta_W * self.learning_rate
        self.b += delta_b * self.learning_rate

    def run_batch(self, start, end):
        if DEBUG: print("start batch: {}->{}".format(start, end))
        # Run current net on all train images
        logits_original = self.logits(self.train_images[start:end])

        # Softmax
        logits = self.softmax(logits_original)

        # Create one hot structure from labels
        one_hot_labels = self.one_hots(self.train_labels[start:end])

        # Calculate loss between real and predicted values
        loss = self.loss(one_hot_labels, logits)

        # Update weights
        delta_weight = self.loss_adjustment(self.train_images[start:end].T, loss)
        # delta_weight = np.einsum("ik,ij->jk", loss, self.train_images)
        delta_bias = self.loss_adjustment(np.ones((1,end-start)), loss).ravel()

        if DEBUG: print(delta_weight)
        if DEBUG: print(delta_bias)
        self.backprop(
            delta_weight * self.learning_rate,
            delta_bias * self.learning_rate
        )
        if DEBUG: print("updated weights")

    def accuracy_function(self, test_images, test_labels):
        """
        Calculates the accuracy of the model against test images and labels
        DO NOT EDIT
        Arguments
        test_images: a normalized NumPy array
        test_labels: a NumPy array of ints
        """
        scores = np.dot(test_images, self.W) + self.b
        predicted_classes = np.argmax(scores, axis=1)
        return np.mean(predicted_classes == test_labels)


def main():
    print("Running...")

    # TO-DO: import MNIST test data
    dl = DataLoader()

    # TO-DO: Create Model with training data arrays that sets up the weights and biases.
    m = Model(dl.train_images, dl.train_labels)

    print("Model built")

    # TO-DO: Run model for number of steps by calling run() each step
    for i in range(int(6e4/m.batch_size)):
        m.run()

    '''
    m.run_to(
        # end=int(1e4)
    )
    '''

    # TO-DO: test the accuracy by calling accuracy_function with the test data
    print("Accuracy:", m.accuracy_function(dl.test_images, dl.test_labels))


if __name__ == '__main__':
    main()
