import argparse
import json
first_file = '/Users/pewspoonmail.ru/python-project-50/gendiff/scripts/file1.json'
second_file = '/Users/pewspoonmail.ru/python-project-50/gendiff/scripts/file2.json'


def generate_diff(first_file, second_file):
    first_file = json.load(open(first_file))
    second_file = json.load(open(second_file))
    items: str
    for key, value in {**first_file, **second_file}.items():
        print(key, '-', value)


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    #parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('-f', '--format', default='stylish', choices=['stylish', 'plain', 'json'],
                        help='set format of output')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
