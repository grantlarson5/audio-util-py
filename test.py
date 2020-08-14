#!/usr/bin/env python3

import argparse

def main():
	parser = argparse.ArgumentParser(description='Convert .wav file to .raw')
	parser.add_argument('file', metavar='filepath',
						help='path of .wav file to be converted')
	args = parser.parse_args()

	filepath = args.file

if __name__ == "__main__":
    main()
