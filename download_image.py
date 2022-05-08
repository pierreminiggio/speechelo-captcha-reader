from base64 import b64encode
from os import mkdir, path
from requests import get

cache_folder = 'cache'

def download_image(url: str) -> str:

    if path.isdir(cache_folder) == False:
        mkdir(cache_folder)
    
    image_path = cache_folder + path.sep + str(b64encode(url.encode('ascii'))) + '.png'

    if path.isfile(image_path) == False:
        image_download_request = get(url, allow_redirects=True)
        open(image_path, 'wb').write(image_download_request.content)

    return image_path
