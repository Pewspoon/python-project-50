import argparse
import json
from itertools import chain


def generate_diff(first_file, second_file):
    first_file = json.load(open('/Users/pewspoonmail.ru/python-project-50/gendiff/scripts/file1.json'))
    second_file = json.load(open('/Users/pewspoonmail.ru/python-project-50/gendiff/scripts/file2.json'))
    result = dict(chain(first_file.items(), second_file.items()))
    res = check_type(result)
    print(res)
    string = []
    for key, value in res.items():
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                string.append(f'  {key}: {value}\n')
            else:
                string.append('- ' + f'{key}: {first_file[key]}\n')
                string.append('+ ' + f'{key}: {second_file[key]}\n')
        elif key in first_file:
            string.append(f'- {key}: {first_file[key]}\n')
        elif key in second_file:
            string.append(f'+ {key}: {second_file[key]}\n')
    string = ''.join(string)
    print(string)


def check_type(item):
    new_dict_with_low_values = {}
    for key, value in item.items():
        if type(key) != type(value):
            new_value = str(value).lower()
            new_dict_with_low_values[key] = new_value
        else:
            new_dict_with_low_values[key] = value
    return new_dict_with_low_values


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    #parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('-f', '--format', default='stylish', choices=['stylish', 'plain', 'json'], help='set format of output')
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
