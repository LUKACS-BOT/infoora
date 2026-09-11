szam1 = float(input("Add meg az első számot: "))
szam2 = float(input("Add meg a második számot: "))
muvelet = input("Add meg a műveletet (+, -, *, /): ")

if muvelet == "+":
    eredmeny = szam1 + szam2
elif muvelet == "-":
    eredmeny = szam1 - szam2
elif muvelet == "*":
    eredmeny = szam1 * szam2
elif muvelet == "/":
    eredmeny = szam1 / szam2
else:
    print("Ismeretlen művelet!")
    exit()

print(szam1, muvelet, szam2, "=", eredmeny)