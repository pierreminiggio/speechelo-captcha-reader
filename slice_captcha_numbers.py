from PIL import Image
from read_captcha_number import read_captcha_number
from typing import List, Optional, Tuple

black_threshold = 50
captcha_character_count = 8
captcha_slice_width = 10

def slice_captcha_numbers(image_path: str) -> List[str]:
    captcha_image = Image.open(image_path).convert('RGB')

    first_black_pixel = get_first_black_pixel_coordinates(captcha_image)
    if first_black_pixel == None:
        raise InvalidImageExceptionclass()

    slice_image_name_prefix = image_path[0: -4]
    slicing_start_x_coordinate = figure_out_slicing_start_x_coordinate(first_black_pixel, captcha_image, slice_image_name_prefix)

    return get_image_slices(captcha_image, slicing_start_x_coordinate, slice_image_name_prefix)

class InvalidImageExceptionclass(Exception):
    pass

def get_first_black_pixel_coordinates(image: Image) -> Optional[Tuple[int]]:
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel_coordinates = (x, y)
            pixel_color = image.getpixel(pixel_coordinates)

            if is_black_pixel(pixel_color):
                return pixel_coordinates

    return None

def is_black_pixel(pixel_color: Tuple[int]) -> bool:
    return pixel_color[0] < black_threshold and pixel_color[1] < black_threshold and pixel_color[2] < black_threshold

def figure_out_slicing_start_x_coordinate(first_black_pixel: Tuple[int], image: Image, slice_image_name_prefix: str) -> int:
    normal_slicing_start_x_coordinate = first_black_pixel[0] - 1
    
    return normal_slicing_start_x_coordinate - 1 if is_back_pixel_part_of_number_1(image, normal_slicing_start_x_coordinate, slice_image_name_prefix) else normal_slicing_start_x_coordinate

def is_back_pixel_part_of_number_1(image: Image, normal_slicing_start_x_coordinate: int, slice_image_name_prefix: str) -> bool:
    image_path = get_single_image_slice(image, normal_slicing_start_x_coordinate, slice_image_name_prefix, 0)

    return read_captcha_number(image_path) == '1'

def get_image_slices(image: Image, slicing_start_x_coordinate: int, slice_image_name_prefix: str) -> List[str]:
    slices: List[str] = []

    for captcha_character_index in range(0, captcha_character_count):
        slice_offset = captcha_slice_width * captcha_character_index
        slices.append(get_single_image_slice(image, slicing_start_x_coordinate + slice_offset, slice_image_name_prefix, captcha_character_index))

    return slices

def get_single_image_slice(image: Image, slice_offset: int, slice_image_name_prefix: str, captcha_character_index: int) -> str:
    height = image.size[1]

    slice_box = (
        slice_offset,
        0,
        slice_offset + captcha_slice_width,
        height
    )
    slice_file_name = slice_image_name_prefix + '_' + str(captcha_character_index) + '.png'
    image.crop(slice_box).save(slice_file_name)

    return slice_file_name