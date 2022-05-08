from download_image import download_image
import sys

args = sys.argv

if len(args) != 2:
    print('Use like this : python main.py <captcha_image_url>')
    sys.exit()

image_path = download_image(args[1])

print(image_path)

# ^ Fait, télécharger l'image

# TODO découper l'image
# TODO Donner les petites images
