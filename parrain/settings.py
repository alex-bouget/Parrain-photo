import os


cache_folder = "cache"
id_parrain_file = "idParrain.json"
img_file = "img.json"
img_size = (450, 600)
img_head_size = (400, 400)
img_folder = "img"

if not os.path.isdir(cache_folder):
    os.mkdir(cache_folder)

if not os.path.isdir(img_folder):
    os.mkdir(img_folder)