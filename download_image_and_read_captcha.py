from download_image import download_image
from read_captcha_number import read_captcha_number
from slice_captcha_numbers import slice_captcha_numbers

def download_image_and_read_captcha(captcha_image_url: str) -> str:

    image_path = download_image(captcha_image_url)
    captcha_numbers = slice_captcha_numbers(image_path)

    captcha = ''

    for captcha_number in captcha_numbers:
        captcha += read_captcha_number(captcha_number)

    return captcha
