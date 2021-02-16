from PIL import Image

from assignment import DataLoader, np


def main():
    # Import MNIST test data
    dl = DataLoader()

    # Load and resize data:
    img_idx = 4
    img_data = (dl.train_images[img_idx].reshape((28,28))*255).astype(np.uint8)

    # Create PIL image and show
    img = Image.fromarray(img_data, 'L')
    img.show()

if __name__ == '__main__':
    main()
