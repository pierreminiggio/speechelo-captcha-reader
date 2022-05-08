from PIL import Image
from typing import List, Optional, Tuple

black_threshold = 50

def slice_captcha_numbers(image_path: str) -> List[str]:
    captcha_image = Image.open(image_path)

    first_black_pixel = get_first_black_pixel_coordinates(captcha_image)
    if first_black_pixel == None:
        raise InvalidImageExceptionclass()
        
    print(first_black_pixel)

    return []

class InvalidImageExceptionclass(Exception):
    pass

def get_first_black_pixel_coordinates(image: Image) -> Optional[Tuple[int]]:
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel_coordinates = (x, y)
            pixel_color = image.getpixel(pixel_coordinates)
            if pixel_color[0] < black_threshold and pixel_color[1] < black_threshold and pixel_color[2] < black_threshold:
                return pixel_coordinates

    return None