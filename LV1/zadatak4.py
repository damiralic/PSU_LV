brojac = 0
lista = []
while True:
    broj=input("Unesi: ")
    if broj == "Done":
        break
    else:
        brojac+=1
        lista.append(int(broj))
    
print("Velicina liste: ", len(lista))
print("Unijeli ste: ", brojac)
print("Srednja vrijednost je: ", len(lista))
print("Najmanja vrijednost je: ", min(lista))
print("Najveca vrijednost je: ", max(lista))

