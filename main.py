import parrain
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Parrain")
    parser.add_argument("-i", "--init", help="Initialize the cache", type=str)
    parser.add_argument("-c", "--create", action="store_true", help="Create the images")
    parser.add_argument("-t", "--tableur", help="Create the tableur", type=str)
    args = parser.parse_args()
    if args.init:
        print("Initializing the cache...")
        parrain.load_cache(args.init)
    if args.create:
        print("Creating the images...")
        parrain.load_image()
    if args.tableur:
        print("Creating the tableur...")
        parrain.create_tableur(args.tableur)

if __name__ == "__main__":
    main()