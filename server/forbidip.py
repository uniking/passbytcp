#!/usr/bin/python
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
                    description='print plist file')
    parser.add_argument(
            '-i', '--ip',
            help='forbid ip'
            )
             
    return parser.parse_args()
             
def main(args):
    if args.ip is None:
        print('-i 10.23.34.0')
        return
    os.system('ptables -I INPUT -s '+args.ip+'/24 -j DROP')

if __name__ == '__main__':
    args = parse_args()
    main(args)
