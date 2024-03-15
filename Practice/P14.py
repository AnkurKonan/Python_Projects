#Accepting Arguments
# import sys
# name = sys.argv[1]
# print(sys.argv)
# print("Hello " + name)

import argparse
parser = argparse.ArgumentParser(
    description='This program print name of dog'
)
parser.add_argument('-c','--color', metavar='color', required=True, help='the color to search for')
args = parser.parse_args()
print(args.color)
