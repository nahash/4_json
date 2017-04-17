# -*- coding: utf-8 -*-
import json
import argparse
import os
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        dump = json.load(file)
    return dump


def pretty_print_json(data, indent=2):
    print(json.dumps(data, indent=indent, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help="File path")
    parser.add_argument('-i', '--indent', type=int, default=2, help="Indent")
    args = parser.parse_args()
    if not os.path.exists(args.filepath):
        print("File not found!")
        sys.exit(2)
    data = load_data(args.filepath)
    if data:
        pretty_print_json(data, args.indent)

