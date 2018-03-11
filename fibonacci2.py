import os
import csv
import time
#Rekurencja, polega na wywolaniu przez funkcje samej siebie. 
#Algorytmy rekurencyjne zastepuje w pewnym sensie iteracje

#Ciag Fibonacciego - ciag liczb naturalnych okreslony rekurencyjnie 
#Pierwszy wyraz jest rowny 0, drugi jest rowny 1, 
#kazdy nastepny jest suma dwoch poprzednich. 

def export_data(filecsv,tab):
	with open (filecsv, "w", newline='') as database:
		writer = csv.writer(database)
		writer.writerow(tab)
def fib_rek(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)

print ("Podaj n-ty wyraz ciagu ktory chcesz poznac: ")
lista2 = []
n = int(input())
x = time.time()
lista2.append(fib_rek(n))
y = time.time()
z = str(y-x)
#append dziala tylko w listach
lista2.append(z)
print(lista2)
export_data("export_fib.csv", lista2)