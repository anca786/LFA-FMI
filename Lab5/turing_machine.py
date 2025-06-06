import json

def simuleaza_turing_machine(config_tm, banda_initiala_str, pasi_maximi=1000):
    stare_initiala = config_tm["stare_initiala"]
    simbol_gol = config_tm["simbol_gol"]
    stari_finale = set(config_tm["stari_finale"])
    tranzitii = config_tm["tranzitii"]

    banda = list(banda_initiala_str.replace(simbol_gol, simbol_gol))
    
    if not banda:
        banda.append(simbol_gol)

    pozitie_cap = 0
    stare_curenta = stare_initiala
    pasi_efectuati = 0

    print(f"Începem simularea: Stare: {stare_curenta}, Bandă: {''.join(banda)}, Cap: {pozitie_cap}")

    while pasi_efectuati < pasi_maximi and stare_curenta not in stari_finale:
        simbol_curent_banda = banda[pozitie_cap]
        gasit_tranzitie = False

        if stare_curenta in tranzitii and simbol_curent_banda in tranzitii[stare_curenta]:
            stare_noua, simbol_scris, directie_miscare = tranzitii[stare_curenta][simbol_curent_banda]
            
            banda[pozitie_cap] = simbol_scris
            stare_curenta = stare_noua

            if directie_miscare == 'D':
                pozitie_cap += 1
                if pozitie_cap >= len(banda):
                    banda.append(simbol_gol)
            elif directie_miscare == 'S':
                pozitie_cap -= 1
                if pozitie_cap < 0:
                    banda.insert(0, simbol_gol)
                    pozitie_cap = 0
            else:
                print(f"Eroare: Direcție de mișcare invalidă '{directie_miscare}' la pasul {pasi_efectuati+1}.")
                return False
            
            gasit_tranzitie = True
            
            print(f"Pas {pasi_efectuati+1}: Stare: {stare_curenta}, Bandă: {''.join(banda)}, Cap: {pozitie_cap}")
            pasi_efectuati += 1
        
        if not gasit_tranzitie:
            break

    acceptata = stare_curenta in stari_finale
    
    print(f"\nSimulare terminată după {pasi_efectuati} pași.")
    print(f"Starea finală: {stare_curenta}")
    print(f"Banda finală: {''.join(banda)}")
    print(f"Mașina a acceptat (stare finală): {acceptata}")
    
    return acceptata



with open('turing_machine.json', 'r') as f: 
    config_tm = json.load(f)
        
        
input_banda_raw = input("Introduceți șirul de intrare pentru bandă: ")
rezultat_simulare = simuleaza_turing_machine(config_tm, input_banda_raw)
print("ACCEPTAT" if rezultat_simulare else "RESPINS")