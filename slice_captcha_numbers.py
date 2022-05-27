from PIL import Image
from read_captcha_number import read_captcha_number
from typing import List, Optional, Tuple

black_threshold = 50
captcha_character_count = 8
captcha_slice_width = 10
captcha_slice_height = 12

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
    image_path = get_single_image_slice(image, normal_slicing_start_x_coordinate, slice_image_name_prefix, 0)
    single_number = read_single_number(image_path)

    if single_number == '1':
        return normal_slicing_start_x_coordinate - 1

    if single_number == '0':
        if are_last_2_columns_empty(image_path):
            return normal_slicing_start_x_coordinate - 1

    return normal_slicing_start_x_coordinate

def read_single_number(image_path: str) -> str: return read_captcha_number(image_path)

def are_last_2_columns_empty(image_path: str) -> bool:
    slice_image = Image.open(image_path).convert('RGB')
    (width, height) = slice_image.size

    for x in range(width - 2, width):
        for y in range(0, height):
            pixel_coordinates = (x, y)
            pixel_color = slice_image.getpixel(pixel_coordinates)
            if is_black_pixel(pixel_color): return False

    return True

def get_image_slices(image: Image, slicing_start_x_coordinate: int, slice_image_name_prefix: str) -> List[str]:
    slices: List[str] = []

    for captcha_character_index in range(0, captcha_character_count):
        slice_offset = captcha_slice_width * captcha_character_index
        slices.append(get_single_image_slice(image, slicing_start_x_coordinate + slice_offset, slice_image_name_prefix, captcha_character_index))

    return slices

def get_single_image_slice(image: Image, slice_offset: int, slice_image_name_prefix: str, captcha_character_index: int) -> str:
    height = image.size[1]
    slice_baseline = find_slice_baseline(image, slice_offset)

    image_x_start = slice_offset
    image_y_start = slice_baseline
    image_x_end = image_x_start + captcha_slice_width
    image_y_end = image_y_start + captcha_slice_height

    # Remove noise
    for x in range(image_x_start, image_x_end):
        for y in range(image_y_start, image_y_end):
            pixel_coordinates = (x, y)
            pixel_color = image.getpixel(pixel_coordinates)
            new_color = (0, 0, 0) if is_black_pixel(pixel_color) else (255, 255, 255)
            image.putpixel(pixel_coordinates, new_color)

    slice_box = (
        image_x_start,
        image_y_start,
        image_x_end,
        image_y_end
    )

    slice_file_name = slice_image_name_prefix + '_' + str(captcha_character_index) + '.png'
    image.crop(slice_box).save(slice_file_name)

    return slice_file_name

def find_slice_baseline(image: Image, slice_offset: int) -> int:
    height = image.size[1]

    for reverse_y in range(height):
        y = height - reverse_y - 1
        for x in range(slice_offset, slice_offset + captcha_slice_width):
            pixel_coordinates = (x, y)
            pixel_color = image.getpixel(pixel_coordinates)

            if is_black_pixel(pixel_color):
                return y - captcha_slice_height + 2

    raise Exception('No slice baseline found')
    
