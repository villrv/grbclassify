from ClassiPyGRB import SWIFT
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
import pandas as pd


swift = SWIFT(res=64)

filename = 'summary.txt'
save = False
load = True

# Grabs all the data from Swift -- FYI this broke at some point
if save:

	counter = 0

	with open(filename) as file:
		for line in file:
			if ('GRB' in line) and ('#' not in line):
				print(line)
				counter = counter+1

				df = swift.obtain_data(name=line.split()[0])
				df.to_pickle('./data/'+line.split()[0]+'.pkl')

# Otherwise, just load in data

if load:

	onlyfiles = [f for f in listdir('./data/') if isfile(join('./data/', f))]
	for f in onlyfiles:
		data = pd.read_pickle("./data/"+f)  
		print(f)
		plt.plot(data['Time(s)'],data['15-25keV'],color='g')
		plt.plot(data['Time(s)'],data['25-50keV'],color='r')
		plt.plot(data['Time(s)'],data['50-100keV'],color='purple')
		plt.plot(data['Time(s)'],data['100-350keV'],color='orange')

		plt.show()
		# Just cancel after 1 plot
		sys.exit()

# Alternatively, plot with ClassiPyGRB
# swift.plot_any_grb(name='GRB210726A')
# plt.show()