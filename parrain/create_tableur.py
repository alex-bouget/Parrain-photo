import csv
import json
import os
from .settings import cache_folder, id_parrain_file

def create_tableur(file_output):
    """Create a tableur from the cache."""
    table = []
    table.append(["IdDiscord", "IdParrain", "Nom"])
    
    parrain = json.load(open(os.path.join(cache_folder, id_parrain_file), "r", encoding="utf-8"))

    for id_discord, parrain_data in parrain.items():
        table.append([id_discord, str(parrain_data[0]), parrain_data[1]])
    print(f"{len(parrain.keys())} parrains loaded.")

    with open(file_output, "w", newline="", encoding="utf-8") as f:
        print(f"Writing the tableur in {file_output}...")
        writer = csv.writer(f)
        writer.writerows(table)