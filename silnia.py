import os
import csv
import time

def export_data(filecsv,tab):
	with open (filecsv, "w") as database:
		writer = csv.writer(database)
		writer.writerow(tab)

def silnia(n):
	data = []
	if n == 0:
		return 1
	else:
		for i in range (1,n):
			n=n*i
			data.append(str(n))
		return data

print("Z jakiej liczby chcesz obliczyc silnie?")
n=int(input())
x = time.time()
tab_silnia = silnia(n)
y = time.time()
z = str(y-x)
tab_silnia.append(z)

export_data("export_silnia.csv", tab_silnia)