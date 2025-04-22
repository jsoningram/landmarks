import os
from src.resize.resize import resize_image
from src.identify.identify import get_landmarks

Resize_Percentage = 25
Dir_Path = './images'


def main():
    # Create list of files in `path`
    files = os.listdir(Dir_Path)

    # Iterate over `files` and resize images
    for file in files:
        if file[-4:].lower() in ['.jpg', 'jpeg', '.png']:
            resize_image(f'{Dir_Path}/{file}', Resize_Percentage)

    get_landmarks()


if __name__ == '__main__':
    main()
