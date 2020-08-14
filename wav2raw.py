#!/usr/bin/env python3

import sys
import argparse
import wave
import os.path

def main():
	parser = argparse.ArgumentParser(description='Convert .wav file to .raw')
	parser.add_argument('file', metavar='filepath',
						help='path of .wav file to be converted')
	args = parser.parse_args()

	filepath = args.file

	# Error checking
	if not os.path.isfile(filepath):
		sys.exit("File " + filepath + " does not exist")

	if not filepath.lower().endswith('.wav'):
		sys.exit("File " + filepath + " is not a .wav file")

	# File processing
	wav = wave.open(filename, 'rb')

	if wav.getnchannels() == 2:
		# TODO - Convert to mono using RMS (see Matlab)



	# TODO - Close Wave_read object using Wave_read.close()










if __name__ == "__main__":
    main()

# import argparse
# import wave




# parser = argparse.ArgumentParser(description='Convert .wav file to .raw')
# parser.add_argument();
#
# # Finish argument parsing
#
# original = wave.open(file,'rb');
#
# if (original.getnchannels() != 1)

# Use exceptions for error handling in Python
