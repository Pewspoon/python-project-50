import argparse
import json
from gendiff.scripts import file1


def generate_diff(first_file, second_file):
    json.load(open(f'path/to/{first_file}'))
    json.load(open(f'path/to/{second_file}'))
    result = {}
    items = (result[x] for x in second_file.items() if x in first_file and second_file)
    return '{\n' + '\n'.join(items) + '\n}'


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
