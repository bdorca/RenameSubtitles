__author__ = "bdorca"
import argparse
import json
import file_rename


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help="JSON of directories", required=True)
    args = parser.parse_args()
    source = args.file
    with open(source) as source_file:
        source_json = json.load(source_file)
        for l in source_json.__getitem__("directories"):
            d = l["dir"]
            episodes = d["episodes"]
            subtitles = d["subtitles"]
            file_rename.doit(episodes, subtitles)


if __name__ == '__main__':
    main()
