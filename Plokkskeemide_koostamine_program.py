from time import *
#V5 3. Rühm 20 õpilast sooritas ühe sessiooni jooksul kolm eksamit. Tehke algoritm eksamivormi täitmiseks.
for õ in range(20):
    print(f"Soritab eksamit {õ+1}. õpilane")
    for e in range(3):
        print(f"{e+1}. eksam")

# #V4 2. Koostage programmi plokkskeem, et arvutada ainult negatiivsete P antud arvude summa.

vastus=0
P=int(input("Mitu korda kordame?"))
while True:
    arv=float(input("Sisesta arv: "))
    if arv<0: vastus+=arv
    P-=1
    if P==0: break
print(f"Summa on {vastus}")

vastus=0
P=int(input("Mitu korda kordame?"))
for i in range(P):
    arv=float(input("Sisesta arv: "))
    if arv<0: vastus+=arv
print(f"Summa on {vastus}")

#V1 4. Koostage plokkskeem kotlette praadiva roboti jaoks.

while True:
    try:
        kokku=int(input("Kokku kotlete: "))
        panni_maht=int(input("Panni maht: "))
        break
    except:
        print("Viga!")
aeg=1
lahenemine=kokku//panni_maht
jaak=kokku%panni_maht
if jaak>0: lahenemine+=1
print(f"Praeme. Tuleb {lahenemine} lahenemist")
for l in range(lahenemine):
    print(f"{l+1}. lahenemine. Praeme esimene pool")
    sleep(aeg)
    print("Ümberpõõrame")
    print(f"{l+1}. lahenemine. Praeme teine pool")
    sleep(aeg)
    print(f"Valmis")
    print(f"L = {l}")
    if jaak>0 and l==lahenemine-1:
        print(jaak)
    else:
        print(panni_maht)


print("Koik kotletid on praetud!")
