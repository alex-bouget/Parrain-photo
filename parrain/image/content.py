from PIL import ImageDraw
from ..settings import img_size

def create_content(draw : ImageDraw, content, font):
    while True:
            box_text = draw.textbbox((0, 0), content, font=font, align="center")
            if box_text[2] > img_size[0]-20:
                frame = content
                index = (
                    frame.rindex("\n")
                    if "\n" in frame
                    else 0
                )
                while True:
                    box_text2 = draw.textbbox((0, 0), content[0:index], font=font, align="center")
                    if box_text2[2] > img_size[0]-20:
                        index = frame.rindex(" ", 0, index)
                        break
                    index += 1
                content = content[0:index] + "\n" + content[index+1:]
            else:
                break
    return content