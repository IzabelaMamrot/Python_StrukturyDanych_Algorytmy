import random
import os
import csv
import time

def get_data(filecsv):
	data = []
	if os.path.isfile(filecsv): 
		with open(filecsv, "r") as database:
			for line in database:
				line = line.replace("\n", "")
				line = line.replace("\r", "")
				data.append(line)
	else:
		print ("File", filecsv, " does not exist!")
	return data
	
#pivot'em jest ostatim element w tablicy, umieszcza pivod w odpowiedniej pozycji w
#posortowanej tablicy i umieszka wszytkie mniejsze wartosci na lewo od pivot,
#a wieksze wartosci na prawo od pivot

def sort(tab,low,high):  #PODZIAL

	i = (low - 1) #zmniejszamy i o 1 poniewaz dlugosc tablicy - 1, da nam indeks
			#indexowanie w tablicy od zera, dlatego ojemujemy -1	
	pivot = tab[high] #pivot na ostatnim miejscu tablicy
	
	for j in range(low, high): #przedzial 
		if tab[j] <= pivot: #jesli element biezacy jest mniejszy/rowny od pivot
			i=i+1 #dodawanie indeksu mniejszego elementu
			tab[i],tab[j]=tab[j],tab[i] #zmiana miejsc?
	tab[i+1],tab[high]=tab[high],tab[i+1]
	return (i+1)
	
#tab[] - tablica do posortowania
#low - indeks poczatkowy
#high - indeks koncowy

def quicksort(tab,low,high):

	if low<high:
		g=sort(tab,low,high) 
		
		#tablica przed posortowaniem i po sortowaniu
		quicksort(tab,low,g-1)
		quicksort(tab,g+1,high)
				
	
def export_data(filecsv,tab):
	with open (filecsv, "a", newline='') as database:
		writer = csv.writer(database)
		writer.writerow(tab)


#n=int(input("Enter number of element : "))
#tab=[]
#print ("Enter values of element")
#for k in range(0,n):
#    x=input()
#    tab.append(x)
#quicksort(tab,0,len(tab)-1)
#print (tab)


while True:
	a=int(input())
	tab=random.sample(range(a), a)
	#print(listau)
	#tablica = get_data("lab1.csv")

	t = time.time()
	posortowane = quicksort(tab,0,len(tab)-1)

	y = time.time()
	z = str(y-t)
	print(z)
	lista_excel = []
	lista_excel.append(a)
	lista_excel.append(z)
	#print(posortowane)
	export_data("export_quick.csv", lista_excel )
	if a == 0:
		break


