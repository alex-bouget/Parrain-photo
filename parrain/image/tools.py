from io import BytesIO
from PIL import Image
import requests



def load_img(url, width, height):
    img = requests.get(url)
    print(url)
    img = Image.open(BytesIO(img.content)).convert("RGB")

    whmax = min(img.size)
    width = width if whmax != img.size[0] else int(
        (img.size[0] / img.size[1]) * width)
    height = height if whmax != img.size[1] else int(
        (img.size[1] / img.size[0]) * height)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    return img

def crop(img, width_crop, height_crop):
    width, height = img.size
    left = 0 if width == width_crop else (width - width_crop) // 2
    top = 0 if height == height_crop else (height - height_crop) // 2
    right = width_crop if width == width_crop else (width + width_crop) // 2
    bottom = height_crop if height == height_crop else (height + height_crop) // 2
    img = img.crop((left, top, right, bottom))
    return img