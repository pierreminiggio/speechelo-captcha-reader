from PIL import Image
from typing import List, Optional, Tuple

black_threshold = 50
captcha_character_count = 8
captcha_slice_width = 10

def slice_captcha_numbers(image_path: str) -> List[str]:
    captcha_image = Image.open(image_path)

    first_black_pixel = get_first_black_pixel_coordinates(captcha_image)
    if first_black_pixel == None:
        raise InvalidImageExceptionclass()

    slicing_start_x_coordinate = figure_out_slicing_start_x_coordinate(first_black_pixel)

    return get_image_slices(captcha_image, slicing_start_x_coordinate, image_path[0: -4])

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

def figure_out_slicing_start_x_coordinate(first_black_pixel: Tuple[int]) -> int:
    return first_black_pixel[0] - 1

def get_image_slices(image: Image, slicing_start_x_coordinate: int, slice_image_name_prefix: str) -> List[str]:
    slices: List[str] = []
    height = image.size[1]

    for captcha_character_index in range(0, captcha_character_count):
        slice_offset = captcha_slice_width * captcha_character_index
        slice_box = (
            slicing_start_x_coordinate + slice_offset,
            0,
            slicing_start_x_coordinate + captcha_slice_width + slice_offset,
            height
        )
        slice_file_name = slice_image_name_prefix + '_' + str(captcha_character_index) + '.png'
        image.crop(slice_box).save(slice_file_name)
        slices.append(slice_file_name)

    return slices
