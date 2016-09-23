#!/usr/bin/python

stimuli_name = "1.10_B48_O52_1_orange.jpg"

class FishStimuli:
	"""
	FishStimuli is experimental stimuli
	object holder suitable for each run.
	It parse stimuli file into specified
	parameters.
	
	Input:
		source = file name of stimuli
	Output:
		source = source
		difficulty = number expressed log
		blues = number of blue fishes
		oragnes = number of orange fishes
		corr = which one is correct
	"""
	# Main class function
	def __init__(self, source):
		self.source = source	# Source
		# Get number of log in difficulty
		base = source[0]
		diff = source[2:3]
		# Join difficulty into integer
		self.difficulty = int(base + diff)
		# Fish cluster numbers
		self.blues = int(source[6:8])	# Blue
		self.oranges = int(source[10:12]) # Orange
		# Decide which is correct
		if self.blues > self.oranges:
			self.corr = "blue"
		else:
			self.corr = "orange"
	
	# Printing function
	def fishInfo(self):
		print((" " * 11) + "Fish stimuli parameters\n" + ("-" * 49))
		print("Source\t\t\t" + self.source)
		print("Difficulty\t\t" + str(self.difficulty))
		print("Number of blue\t\t" + str(self.blues))
		print("Number of orange\t" + str(self.oranges))
		print("Correct one\t\t" + self.corr)

# How to use this
a = FishStimuli(stimuli_name)
a.fishInfo()
