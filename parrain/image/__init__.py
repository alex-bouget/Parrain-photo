import json
import os
from .content import create_content
from .img import create_img
from ..settings import cache_folder, id_parrain_file, img_file, img_folder, img_size, img_head_size
from PIL import ImageDraw, ImageFont

def load_image():
    img_json = json.loads(open(os.path.join(cache_folder, img_file), "r", encoding="utf-8").read())
    id_parrain = json.loads(open(os.path.join(cache_folder, id_parrain_file), "r", encoding="utf-8").read())
    for parrain in id_parrain.keys():
        i = 0
        for filleul in img_json[parrain]:
            img = create_img(filleul["img"])
            
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("Montserrat-Black.otf", 20)
            content = create_content(draw, filleul["content"], font)
            if content == "":
                content = "..."
            draw.text((img_size[0]-25, 0), str(id_parrain[parrain][0]), (0, 0, 0), font=font, align="center")
            draw.text(
                (
                img_size[0]/2,
                img_head_size[1]+((img_size[1]-img_head_size[1])//2)
                ),
                content,
                (0, 0, 0),
                align="center",
                anchor="mm",
                font=font)
            img.save(os.path.join(img_folder, f"{id_parrain[parrain][0]}-{i}.png"))
            i += 1