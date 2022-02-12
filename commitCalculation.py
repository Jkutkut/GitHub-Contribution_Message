#!/bin/env python3

import sys
from datetime import datetime, timedelta

data=open("testing/txt").read().split("\n")[:-1]
endDate = datetime.today()
debug = False

# Argument analysis
i = 0
while i < len(sys.argv):
	if sys.argv[i].startswith("--end-date="):
		d = [int(j) for j in sys.argv[i][11:].split("/")]
		endDate = datetime(d[2], d[1], d[0])
	if sys.argv[i] == "--debug":
		debug = True
	i += 1

endDate = endDate.replace(hour=0, minute=42, second=42)

# Analyse the data
endDateWD = endDate.weekday()
firstMonday = endDate - timedelta(days=endDateWD + 7) - timedelta(days=7 * len(data[0]))

if debug:
	print(f"End date: {endDate.strftime('%d/%m/%y')}")
	dataStr = "\n".join(data)
	print(f"Data:\n{dataStr}")
	print(f"End date weekday: {endDateWD}")
	print(f"First Monday: {firstMonday.strftime('%d/%m/%y')}")

for r in range(len(data)):
	for c in range(len(data[0])):
		if not data[r][c] == " ":
			for commit in range(int(data[r][c])):
				# Sat Feb 12 18:18:41 2022 +0100
				d = firstMonday - timedelta(days=7*r + c)
				print(f"{d.strftime('%a %b %d %H:%M:%S %Y +0100')}")