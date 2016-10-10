# -*- coding: utf-8 -*-

import json
import argparse

def load_data(filepath):
    with open(filepath) as data_file:
        data = json.load(data_file)
    return data

def pretty_print_json(data):
    return json.dumps(data,indent=4, sort_keys=True,ensure_ascii=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    file_name = parser.parse_args().file_name
    data = load_data(file_name)
    print('Ваш файл c данными: {}'.format(file_name))
    print(pretty_print_json(data))
