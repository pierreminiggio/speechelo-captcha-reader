from download_image_and_read_captcha import download_image_and_read_captcha
import sys

args = sys.argv

if len(args) != 2:
    print('Use like this : python main.py <captcha_image_url>')
    sys.exit()

print(download_image_and_read_captcha(args[1]))
