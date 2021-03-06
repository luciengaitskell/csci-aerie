import numpy as np
import os
# Killing optional CPU driver warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


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
        input_size, num_classes, batchSz, learning_rate = 784, 10, 1, 0.5
        self.train_images = train_images
        self.train_labels = train_labels
        # sets up weights and biases...
        self.W = _
        self.b = _

    def run(self):
        """
        Does the forward pass, loss calculation, and back propagation 
        for this model for one step
        Args: None
        Return: None
        """
        pass

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
    # TO-DO: import MNIST test data

    # TO-DO: Create Model with training data arrays that sets up the weights and biases.

    # TO-DO: Run model for number of steps by calling run() each step

    # TO-DO: test the accuracy by calling accuracy_function with the test data


if __name__ == '__main__':
    main()
