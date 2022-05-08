import pytesseract
import cv2

def read_captcha_number(file_path: str) -> str:
    img = cv2.imread(file_path)
    
    return pytesseract.image_to_string(img, config='--psm 7 -c tessedit_char_whitelist=0123456789').strip()
