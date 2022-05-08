from download_image import download_image
from read_captcha_number import read_captcha_number
from slice_captcha_numbers import slice_captcha_numbers
import sys

args = sys.argv

if len(args) != 2:
    print('Use like this : python main.py <captcha_image_url>')
    sys.exit()

image_path = download_image(args[1])
captcha_numbers = slice_captcha_numbers(image_path)

captcha = ''

for captcha_number in captcha_numbers:
    captcha += read_captcha_number(captcha_number)

print(captcha)
