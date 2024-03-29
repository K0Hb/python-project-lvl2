import argparse


def cli_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output by selecting\
                             from[stylish, plain, json]\
                               (default: stylish)')
    return parser.parse_args()
