# Parrain-photo
Script de construction des parrain

## Installation

```bash
git clone https://github.com/MisterMine01/Parrain-photo.git
```

Récupérer les data sur le serveur discord avec
[DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) et les sauvegarder en .csv

```
python main.py -i <csv>
```

## Options

```
usage: main.py [-h] [-i CSV] [-c] [-t json_file]

-h: Affiche l'aide
-i: Créer le cache à partir du fichier csv
-c: Générer les images
-t: Générer le json des codes de parrains
```

## Exemple

```
python main.py -i data.csv -c -t parrain.json
```
```
python main.py -i data.csv
# change cache if you want
python main.py -c
```