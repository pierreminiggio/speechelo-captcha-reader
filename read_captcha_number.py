from pytesseract import image_to_string
from cv2 import imread

def read_captcha_number(file_path: str) -> str:
    return image_to_string(imread(file_path), config='--psm 7 -c tessedit_char_whitelist=0123456789').strip()
