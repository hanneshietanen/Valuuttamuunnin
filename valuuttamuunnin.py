## Valuuttamuunnin
## 24.10.2014
## AR, JL, HH

## Valuuttakurssit
euroDollareiksi = 1.2669
euroPunnaksi = 0.79040
dollariEuroiksi = 0.7903
dollariPunnaksi = 0.6229
puntaEuroiksi = 1.2675
puntaDollareiksi = 1.6056

print("Valuuttamuunnin")
print("Mista valuutasta haluat muuttaa ja mihin?")
print("1) Eurosta dollariksi")
print("2) Eurosta punnaksi")
print("3) Dollarista euroksi")
print("4) Dollarista punnaksi")
print("5) Punnasta euroksi")
print("6) Punnasta dollariksi")
valinta = int(input("Valintasi: "))

luku = float(input("Anna rahamaara: "))

if valinta == 1:
  print(luku, "euroa on dollareina", round(luku * euroDollareiksi, 2))
elif valinta == 2:
  print(luku, "euroa on punnissa", round(luku * euroPunnaksi, 2))
elif valinta == 3:
  print(luku, "dollaria on euroina", round(luku * dollariEuroiksi, 2))
  
elif valinta == 5:
  print(luku, "puntaa on euroina", round(luku * puntaEuroiksi, 2))
 


