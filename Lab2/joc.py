import json

def joaca_joc(date_joc, secventa_directii):
    tranzitii = {}
    for ruta in date_joc["routes"]:
        inc = ruta["inc"]
        simbol_directie = ruta["state"]
        fin = ruta["fin"] 
        if inc not in tranzitii:
            tranzitii[inc] = {}
        tranzitii[inc][simbol_directie] = fin
    stare_curenta = date_joc["start"][0]
    are_lingura = 0 
    print("\n--- Începutul Jocului ---")
    print(f"Te afli în: {stare_curenta}")
    harta_directii = {
        "0": "sus", 
        "1": "jos", 
        "2": "dreapta", 
        "3": "stânga"
    }
    for directie_char in secventa_directii:
        directie_text = harta_directii.get(directie_char, f"necunoscută ({directie_char})")
        print(f"\nÎncerc să mă mișc {directie_text} din '{stare_curenta}'...")
        urmatoarea_stare_posibila = tranzitii.get(stare_curenta, {}).get(directie_char)
        if urmatoarea_stare_posibila:
            stare_curenta = urmatoarea_stare_posibila
            print(f"Ai ajuns în: {stare_curenta}")
        else:
            print(f"Nu te poți mișca {directie_text} din '{stare_curenta}'. Rămâi în aceeași stare.") 
        if stare_curenta == "Bucatarie":
            if are_lingura == 0:
                are_lingura = 1
                print("Ai găsit lingura în Bucătărie! Acum o ai.")
    print("\n--- Rezultate Finale ---")
    print(f"Starea finală: {stare_curenta}")
    print(f"Ai lingura? {'DA' if are_lingura == 1 else 'NU'}")
    stare_finala_joc = date_joc["final"][0] 
    if stare_curenta == stare_finala_joc and are_lingura == 1:
        print("Felicitări! Ai câștigat!")
    elif stare_curenta == stare_finala_joc and are_lingura == 0:
        print("Din păcate, ai ajuns la ieșire, dar nu ai lingura!")
    elif stare_curenta != stare_finala_joc and are_lingura == 1:
        print("Din păcate, nu ai găsit ieșirea!")
    else:
        print("Ai pierdut! Nu ai găsit ieșirea și nu ai lingura.")

with open('joc.json', 'r', encoding='utf-8') as f: 
    date_joc = json.load(f)

print("--------------Meniu----------------")
print("Camerele sunt:")
for x in date_joc["states"]:
    print(x)
print("---------------------------------------------")
print("Direcțiile sunt:")
harta_directii_meniu = {
    "0": "Sus", "1": "Jos", "2": "Dreapta", "3": "Stânga"
}
for x in date_joc["sigma"]:
    print(f"{x}: {harta_directii_meniu.get(x, 'Necunoscută')}")
print("---------------------------------------------")
print("Ai apărut la:")
for x in date_joc["start"]:
    print(x)
print("-----------------------------------------------")
print("Pentru a câștiga trebuie să ajungi la:")
for x in date_joc["final"]:
    print(x)
print("--------------------------------------------------")
print("Reguli Adiționale:")
print("Ai nevoie de lingură pentru a putea ieși. Succes la găsirea ei!")

secventa_input = input("Introdu secvența de direcții (ex: 0213): ")

joaca_joc(date_joc, secventa_input)
