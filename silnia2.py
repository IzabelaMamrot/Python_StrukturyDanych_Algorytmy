import os
import csv
import time

def export_data(filecsv,tab):
	with open (filecsv, "w") as database:
		writer = csv.writer(database)
		writer.writerow(tab)

def silnia(n):
	
	if n == 0:
		return 1
	
	return n*silnia(n-1)

print("Z jakiej liczby chcesz obliczyc silnie?")
lista =[]
n=int(input())
x = time.time() #czas biezacy
lista.append(silnia(n))
y = time.time()#czas biezacy
z = str(y-x)
lista.append(z)
print(lista)

export_data("export_silnia.csv", lista)