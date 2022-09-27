import csv
import json
import os
from .settings import cache_folder, id_parrain_file, img_file


def load_cache(csv_file):
    """Load the cache from a csv file."""
    if not os.path.isfile(csv_file):
        raise Exception("File not found: {}".format(csv_file))
    discord_data = csv.reader(open(csv_file, "r", encoding="utf-8"))
    if os.path.isfile(os.path.join(cache_folder, id_parrain_file)):
        id_parrain = json.load(open(os.path.join(cache_folder, id_parrain_file), "r", encoding="utf-8"))
    else:
        id_parrain = {}
    img = {}
    if len(id_parrain) > 0:
        i=max(x[0] for x in id_parrain.values())+1
    else:
        i=1
    for row in discord_data:
        if row[0] == 'AuthorID':
            continue
        if row[4] == "":
            continue
        if row[1] not in img.keys():
            img[row[1]] = []
            if row[1] not in id_parrain.keys():
                id_parrain[row[1]] = [i, row[1].split("#")[0]]
                i += 1
        img[row[1]].append({"img": row[4], "content": row[3]})
    json.dump(id_parrain, open(os.path.join(cache_folder, id_parrain_file), "w", encoding="utf-8"))
    json.dump(img, open(os.path.join(cache_folder, img_file), "w", encoding="utf-8"))