from pytesseract import image_to_string
from cv2 import imread

def read_captcha_number(file_path: str) -> str:
    image = imread(file_path)
    read_character = image_to_string(image, config='--psm 7 -c tessedit_char_whitelist=oO0123456789').strip().replace('o', '0').replace('O', '0')

    if read_character == '00':
        return '0'

    if read_character == '':
        return '0'

    if read_character == '4':
        check_non_4_char = image_to_string(image, config='--psm 7 -c tessedit_char_blacklist=4').strip()

        if check_non_4_char == 'A': return '7'

    if read_character == '3':
        check_non_3_char = image_to_string(image, config='--psm 7 -c tessedit_char_blacklist=3').strip()

        if check_non_3_char == '5)': return '5'

    return read_character
