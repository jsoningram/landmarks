import csv
import os
from src.utils.vision import generate_image_description

Csv_Path = 'landmarks.csv'


def write_csv(file, landmarks):
    file_exists = os.path.isfile(Csv_Path)

    # Open file in `a` (append mode) so we can keep writing to it
    with open(Csv_Path, 'a', newline='') as output:
        fieldnames = [
            'Image',
            'Description',
            'Confidence Score',
            'Longitude',
            'Latitude',
            'Ref'
        ]

        writer = csv.DictWriter(output, fieldnames=fieldnames)

        # Write headers to CSV file, but only on file creation
        if not file_exists:
            writer.writeheader()

        if len(landmarks) > 0:
            for landmark in landmarks:
                lat = landmark.locations[0].lat_lng.latitude
                long = landmark.locations[0].lat_lng.longitude

                # Write entry to CSV
                writer.writerow(
                    {
                        'Image': file,
                        'Description': landmark.description,
                        'Confidence Score': landmark.score,
                        'Longitude': long,
                        'Latitude': lat,
                        'Ref': f'https://www.google.com/maps/?q={lat},{long}'
                    }
                )
        else:
            description = generate_image_description(file)

            writer.writerow(
                {
                    'Image': file,
                    'Description': description,
                    'Confidence Score': '',
                    'Longitude': '',
                    'Latitude': '',
                    'Ref': ''
                }
            )
