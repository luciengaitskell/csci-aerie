import gzip
import numpy as np
import os
import os.path

# Killing optional CPU driver warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

ROOT = os.path.dirname(os.path.abspath(__file__))

TRAIN_FILE = './train-images-idx3-ubyte.gz'
TRAIN_LABELS = './train-labels-idx1-ubyte.gz'
TEST_FILE = './t10k-images-idx3-ubyte.gz'
TEST_LABELS = './t10k-labels-idx1-ubyte.gz'

def _read32(bytestrm):
    dt = np.dtype(np.uint32).newbyteorder('>')
    return np.frombuffer(bytestrm.read(4), dtype=dt)[0]

class Model:
    """
        This model class provides the data structures for your NN, 
        and has functions to test the three main aspects of the training.
        The data structures should not change after each step of training.
        You can add to the class, but do not change the 
        stencil provided except for the blanks.
        Make sure that these functions work with a loop to call them multiple times,
        instead of implementing training over multiple steps in the function
        Arguments: 
        train_images - NumPy array of training images
        train_labels - NumPy array of labels
    """
    def __init__(self, train_images, train_labels):
        self.input_size, self.num_classes, self.batch_size, self.learning_rate = 784, 10, 2, 0.5
        # imports from images and labels files...
        # sets up weights and biases...
        self.train_images = train_images
        self.train_labels = train_labels

        self.W = np.zeros((self.input_size, self.num_classes))
        self.b = np.zeros((1, self.num_classes))
        self.softmax = 0

    def forward_pass(self):
        """
        Does one forward pass on the images and labels
        :return: None
        """
        
        # picks a random image 
        #print(self.train_images.shape[0]) # this is 60,0000
        #print(self.batch_size) # this is 1
        # Generates a random array of len 1 (batch size) with the values being from 0 to 60k
        indices = np.random.choice(self.train_images.shape[0], self.batch_size)
        #print(indices)
        self.x = self.train_images[indices].astype(np.float32, copy=False)
        self.y = np.array(self.train_labels[indices])

        # Forward Propagation
        # print(self.x.shape) #1 x 784 
        # print(self.W.shape) #784 x 10 
        # print(self.b.shape) # 1 x 10 
        self.logits = np.dot(self.x, self.W) + self.b
        # print(self.logits.shape) # 1 x 10
        self.softmax = np.exp(self.logits) / np.sum(np.exp(self.logits), axis=1).reshape((-1, 1))
        #print(self.softmax.shape) # 1 x 10

        return

    def loss_function(self):
        """
        Calculates the model cross-entropy loss after one forward pass
        :return: the loss of the model as a tensor
        """
        # print(self.batch_size) # 1 
        # print(self.y) # the correct label for the image)
        p = self.softmax[range(self.batch_size), self.y]
        #print(p)
        loss = -np.log(p)
        #loss = np.sum(-np.log(p)) / self.batch_size
        #print(loss)
        return loss

    def back_propagation(self):
        """
        Updates Weights and biases after one forward pass and loss calculation
        :return: None
        """
        # Back Propagation (dL/dlogits is just softmax - 1(y = k) -> softmax minus label indicator)
        dlogits = self.softmax
        dlogits[range(self.batch_size), self.y] -= 1
        #print(dlogits)
        dlogits /= self.batch_size

        # Parameter Gradients (W, b)
        dW = np.dot(self.x.T, dlogits)
        dB = np.sum(dlogits, axis=0, keepdims=True)

        # Update Parameters with Gradients * Learning Rate
        self.W += -self.learning_rate * dW
        self.b += -self.learning_rate * dB

    def run(self):
        self.forward_pass()
        self.loss_function()
        self.back_propagation()

    def accuracy_function(self, test_images, test_labels):
        """
            DO NOT EDIT
            Arguments
            test_images: a normalized NumPy array
            test_labels: a NumPy array of ints
        """
        logits = np.dot(test_images, self.W) + self.b
        predicted_classes = np.argmax(logits, axis=1)
        return np.mean(predicted_classes == test_labels)

def main():
    with open(TRAIN_FILE, 'rb') as f, gzip.GzipFile(fileobj=f) as bytestream:
        _read32(bytestream)
        num_images = _read32(bytestream)
        rows = _read32(bytestream)
        cols = _read32(bytestream)
        buf = bytestream.read(rows * cols * num_images)
        train_images = np.frombuffer(buf, dtype=np.uint8) / 255.0
        train_images = train_images.reshape(num_images, 784)
    with open(TRAIN_LABELS, 'rb') as f, gzip.GzipFile(fileobj=f) as bytestream:
        _read32(bytestream)
        num_items = _read32(bytestream)
        buf = bytestream.read(num_items)
        labels = np.frombuffer(buf, dtype=np.uint8)

    with open(os.path.join(ROOT, TEST_FILE), 'rb') as f, gzip.GzipFile(fileobj=f) as bytestream:
        _read32(bytestream)
        num_images = _read32(bytestream)
        rows = _read32(bytestream)
        cols = _read32(bytestream)
        buf = bytestream.read(rows * cols * num_images)
        test_images = np.frombuffer(buf, dtype=np.uint8) / 255.0
        test_images = test_images.reshape(num_images, 784)

    with open(os.path.join(ROOT, TEST_LABELS), 'rb') as f, gzip.GzipFile(fileobj=f) as bytestream:
        _read32(bytestream)
        num_items = _read32(bytestream)
        buf = bytestream.read(num_items)
        test_labels = np.frombuffer(buf, dtype=np.uint8)

    print(train_images)

    model = Model(train_images, labels)
    # for testing its just 5 but it should be 10k
    steps = int(1e4)
    for i in range(steps):
        model.run()
    print("Accuracy: {}".format(model.accuracy_function(test_images, test_labels)))


if __name__ == '__main__':
    main()
