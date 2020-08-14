#!/usr/bin/env python3

import sys
import wave
import os.path

class Wavy:

	# # Wrapper for printing to stderr
	# def __eprint(*args **kwargs):
	# 	print(*args, file=sys.stderr, **kwargs)

	def __init__ (self, filepath):

		if not os.path.isfile(filepath):
			sys.exit("File " + filepath " does not exist")

		## TODO - Do some exception handling with try except here
 		if not filepath.lower().endswith('.wav'):
			sys.exit("File " + filepath + " is not a .wav file")

		try:
			self.__wav = wave.open(filepath, 'rb')
		except wave.Error:
			sys.exit("An error occured while loading wave file")

		## TODO - Store class data in the format needed by the wav write object
		## this needs to be done such that the class can load something in, do
		## mulptiple rounds of manipulation, then write something away
		self.__nframes = self.__wav.getnframes(void)
		self.__frames = self.__wav.readframes(__nframes)

	def write(filepath):

		# Error checking
		if os.path.isfile(filepath):
			sys.exit("File " + filepath + " already exists")

	def getChannels():

	def setChannels(self, sampleRate):

	def setSampleRate(self, sampleRate):


	def setSampleWidth(self, sampleWidth):
