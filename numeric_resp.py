import csv


def get_numrespdict():
	numrespdict = {}
	numrespfile = open('numeric_resp.csv','rb')
	numrespreader = csv.reader(numrespfile,delimiter=',')
	for row in numrespreader:
		numrespdict[row[0]] = row[1]
	return numrespdict
