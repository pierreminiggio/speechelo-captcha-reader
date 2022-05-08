from pytesseract import image_to_string
from cv2 import imread

def read_captcha_number(file_path: str) -> str:
    read_character = image_to_string(imread(file_path), config='--psm 7 -c tessedit_char_whitelist=oO0123456789').strip().replace('o', '0').replace('O', '0')
    
    return read_character if read_character != '' else '0'
