import argparse


def cli_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='author_format',
                        choices=['author_format', 'plain', 'json'],
                        help='set format of output by selecting\
                             from[author_format, plain, json]\
                               (default: author_format)')
    return parser.parse_args()
