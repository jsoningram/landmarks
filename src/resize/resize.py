from PIL import Image
import os

# Any image over this size will be reduced by `percentage`
Max_Size = 512
Dir_Path = './resized'


def resize_image(image_path, percentage):
    """Resizes an image by a given percentage.

    Args:
        image_path: Path to the image file.
        percentage: Percentage to resize the image (e.g., 50 for 50%).
    """
    try:
        with Image.open(image_path) as img:
            width, height = img.size

            image_name = image_path.split('/')[2]

            # Only resize images that are potentially too large
            if width > Max_Size or height > Max_Size:
                resized_img = img.resize((
                    int(width * (percentage / 100)),
                    int(height * (percentage / 100))
                ))
            else:
                resized_img = img

            # Check if target directory exists. If not, create it
            if not os.path.exists(Dir_Path):
                os.mkdir(Dir_Path)

            # Save the image
            resized_img.save(f'{Dir_Path}/{image_name}')
    except Exception as e:
        print(f'An error occurred while resizing {image_name}', e)
