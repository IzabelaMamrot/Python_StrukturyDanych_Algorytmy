import os
import csv
import time

def export_data(filecsv,tab):
	with open (filecsv, "w", newline='') as database:
		writer = csv.writer(database)
		writer.writerow(tab)

def fib_rek(n):
	lista = [1,1]
	if n < 1:
		lista.pop[1]
	elif n < 3:
		pass
	else:
		for i in range (2,n):
			lista.append(lista[i-1]+lista[i-2])
	return lista

print ("Podaj n-ty wyraz ciagu ktory chcesz poznac: ")
n = int(input())
x = time.time()
lista2 = fib_rek(n)
y = time.time()
z = str(y-x)
lista2.append(z)

export_data("export_fib.csv", lista2)