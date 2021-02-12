import numpy as np
from pathlib import Path
import requests
import gzip
import os
import io
# Killing optional CPU driver warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

PACKAGE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(PACKAGE_DIR, "bin")

class DataLoader:
    URL_TRAIN_IMAGE = "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
    URL_TRAIN_LABEL = "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz"
    URL_TEST_IMAGE = "http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz"
    URL_TEST_LABEL = "http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz"

    def __init__(self):
        """  """
        self.data_path = Path(DATA_DIR)
        self.train_images = self._load_from_url(self.URL_TRAIN_IMAGE, header=16, dsize=784)
        self.train_labels = self._load_from_url(self.URL_TRAIN_LABEL, header=8, dsize=1)
        self.test_images = self._load_from_url(self.URL_TEST_IMAGE, header=16, dsize=784)
        self.test_labels = self._load_from_url(self.URL_TEST_LABEL, header=8, dsize=1)

    def _download(self, url):
        r = requests.get(url)
        return io.BytesIO(r.content)

    def _load_fdata(self, fstream, header, dsize):
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

        return data.reshape(-1, dsize)

    def _load_from_url(self, url, header, dsize):
        return self._load_fdata(self._download(url), header=header, dsize=dsize)

