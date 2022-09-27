from ..settings import img_folder, img_size, img_head_size
from .tools import load_img, crop
from PIL import Image, ImageDraw, ImageFont

def create_img(img_url):
    """Create an image with a head and a body."""
    img = Image.new("RGBA", img_size, (255, 255, 255, 255))
    img_head = load_img(img_url, img_head_size[0], img_head_size[1])
    img_head = crop(img_head, img_head_size[0], img_head_size[1])
    pasting = (min(img_size[0], img_size[1]) - min(img_head_size[0], img_head_size[1]))//2
    img.paste(img_head, (pasting, pasting))
    return img