
print("base max 42")
strr = str(input("entrez la valeur a convertir : "))
base = int(input("en quelle base est la valeur : "))
baseOut = int(input("en quelle base convertir : "))

conv = 0

def convB1ToB2 (strr, base, baseOut, carac = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","²","*","/","+","-","∞"]):
##											   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  42

	strr = strr.upper()
	if base <= 1 or baseOut <= 1 :
		return "Error : base cannot be less than 1"
	if base == baseOut :
		return strr

	nb = 0
	nbOut = ""
	indice = 0

	for i in range(0,len(strr)):

		indice -= 1
		for i in range(0, len(carac)):
			if strr[indice] == carac[i] or carac[i] == carac[base-1]:
				nb += i*(base**((indice+1)*-1))
				break

	if baseOut == 10 :
		return nb

	indice = 0
	while nb // baseOut**indice >= baseOut :
		indice += 1

	while indice != -1 :
		if nb//baseOut**indice <= baseOut :
			nbOut += str(carac[nb//baseOut**indice])
			nb -= baseOut**indice*(nb//baseOut**indice)
		else :
			nbOut += "0"
		indice -= 1

	return nbOut

nb = convB1ToB2(strr, base, baseOut)
print("resultat :",nb)