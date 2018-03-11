import random
import os
import csv
import time

#zapis do pliku
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
	

def sort(tab):  
	# ustawiamy ze nasza petla bedzie wykonywac sie tyle razy ile wynosi 
	# dlugosci listy
	for i in range(len(tab)): 	
		# zmniejszamy j o 1 poniewaz dlugosc tablicy - 1, da nam indeks 
		# ostatniej wartosci w tablicy
		j=len(tab)-1
		#print("nasze i = ", i, "nasze j = ",j)
		while j>i:		#3>0, 2>0, 1>0
			if tab[j]<tab[j-1]: #2<0 -> False
				tmp=tab[j]
				tab[j]=tab[j-1]
				tab[j-1]=tmp 
			j-=1 
		#	print ("nasze j po wykonaniu petli = ",j)
	return tab

    # [1,3,0,2]
    # [1,0,3,2]
    # [0,1,3,2]
    # po drugim forze
    # [0,1,2,3]
    
    
    
def export_data(filecsv,tab):
	with open (filecsv, "a", newline='') as database:
		writer = csv.writer(database)
		writer.writerow(tab)
while True:
	a=int(input())
	listau=random.sample(range(a), a)
	#print(listau)
	#tablica = get_data("lab1.csv")

	x = time.time()
	posortowane = sort(listau)

	y = time.time()
	z = str(y-x)
	print(z)
	lista_excel = []
	lista_excel.append(a)
	lista_excel.append(z)
	#print(posortowane)
	export_data("export_bubble.csv", lista_excel )
	if a == 0:
		break