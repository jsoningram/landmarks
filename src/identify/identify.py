import os
from google.cloud import vision
from src.csv.csv import write_csv

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'
Dir_Path = './resized'


def get_landmarks():
    # Create list of files in `path`
    files = os.listdir(Dir_Path)

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Iterate over `files`
    # @todo We're excluding `.DS_Store` but we should be more specific
    for file in files:
        if '.DS_Store' != file:
            try:
                with open(f'{Dir_Path}/{file}', 'rb') as image_file:
                    content = image_file.read()

                    image = vision.Image(content=content)

                    # Performs landmark detection on the image file
                    response = client.landmark_detection(image=image)
                    landmarks = response.landmark_annotations
            except Exception as e:
                print(
                    f'An error occurred while identifing landmark for {file}',
                    e
                )
            else:
                write_csv(file, landmarks)
