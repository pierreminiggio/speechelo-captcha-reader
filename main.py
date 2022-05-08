from download_image import download_image
from slice_captcha_numbers import slice_captcha_numbers
import sys

args = sys.argv

if len(args) != 2:
    print('Use like this : python main.py <captcha_image_url>')
    sys.exit()

image_path = download_image(args[1])
captcha_numbers = slice_captcha_numbers(image_path)
print(captcha_numbers)

# TODO Donner les petites images
