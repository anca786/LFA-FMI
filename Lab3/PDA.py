import json

with open('PDA.json', 'r') as f:
    config_pda = json.load(f)

stare_curenta = config_pda["start"]
stiva = []

for ruta in config_pda["routes"]:
    if ruta["inc"] == stare_curenta and ruta["read"] == "ε" and ruta["pop"] == "ε":
        if ruta["push"] != "ε":
            stiva.append(ruta["push"])
        stare_curenta = ruta["fin"]
        break

sir_intrare = input("Introdu șirul: ")

for caracter in sir_intrare:
    gasit = False
    varf_stiva = stiva[-1] if stiva else "ε"
    for ruta in config_pda["routes"]:
        if ruta["inc"] == stare_curenta and ruta["read"] == caracter:
            if ruta["pop"] == "ε" or (varf_stiva == ruta["pop"]):
                if ruta["pop"] != "ε":
                    if not stiva or stiva[-1] != ruta["pop"]:
                        print("Respins")
                        exit()
                    stiva.pop()
                if ruta["push"] != "ε":
                    stiva.append(ruta["push"])
                stare_curenta = ruta["fin"]
                gasit = True
                break
    if not gasit:
        print("Respins")
        exit()

for ruta in config_pda["routes"]:
    if ruta["inc"] == stare_curenta and ruta["read"] == "ε":
        if stiva and stiva[-1] == ruta["pop"]:
            stiva.pop()
            if ruta["push"] != "ε":
                stiva.append(ruta["push"])
            stare_curenta = ruta["fin"]
            break

if stare_curenta in config_pda["final"] and not stiva:
    print("Acceptat")
else:
    print("Respins")