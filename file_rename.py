__author__ = "bdorca"
import argparse
from os import listdir, rename
from os.path import isfile, join


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--episodes', help='directory of episodes', required=True)
    parser.add_argument('-s', '--subtitles', help='subtitle directory', required=True)
    args = parser.parse_args()
    print(args.episodes)
    doit(args.episodes, args.subtitles)


def doit(de, ds):
    episodes = [f for f in listdir(de) if isfile(join(de, f))]
    subtitles = [f for f in listdir(ds) if isfile(join(ds, f))]
    episodes.sort()
    subtitles.sort()
    if len(episodes) != len(subtitles):
        exit(1)
    for x in range(0, len(episodes)):
        print(episodes[x])
        print(subtitles[x])
        rename(ds + "\\" + subtitles[x], ds + "\\" + episodes[x][:-4] + subtitles[x][-4:])


if __name__ == '__main__':
    main()
