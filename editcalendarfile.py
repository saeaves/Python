#!/usr/bin/env python3
#Copies a specified .ics file and adds notifications to each calendar option listed.
import os
import fileinput

fileName = input("Please enter the name of the calendar (ics file):")

try:
	infile = open(f'{fileName}.ics', 'rt')
	outfile = open(f'{fileName}-1.ics', 'wt')
except:
	print("File not found!")
	
for line in infile:
	#Replaces END:VEVENT, so it needs to be included.
	if line.startswith("END:VEVENT"):
		#Add ALARM, -P1DT12H0M0S is for 1 Day 12 Hours before
		print("BEGIN:VALARM\nACTION:DISPLAY\nDESCRIPTION:This is an event reminder\nTRIGGER:-P1DT12H0M0S\nEND:VALARM\nEND:VEVENT", file=outfile)
	#else, copy line
	else:
		print(line.rstrip(), file=outfile)
outfile.close()	

print("Done!")
