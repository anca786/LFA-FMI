import json

def epsilon_closure(nfa_data, states):
    closure = set(states)
    stack = list(states) 

    while stack:
         current_state = stack.pop()
         for route in nfa_data.get("routes", []):
            if route.get("inc") == current_state and route.get("state") == "ε":
                for next_state in route.get("fin", []):
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
    return closure

def simulate_nfa(nfa_data, input_string):
    
    stari_initiale= set(nfa_data.get("start", []))
    stari_curente = epsilon_closure(nfa_data, stari_initiale)

    for char in input_string:
        stari_noi = set()
        for state in stari_curente:
            for route in nfa_data.get("routes", []):
                if route.get("inc") == state and route.get("state") == char:
                    stari_noi.update(route.get("fin", []))
        
        stari_curente = epsilon_closure(nfa_data, stari_noi)
    
    stari_finale = set(nfa_data.get("final", []))
    return bool(stari_curente.intersection(stari_finale))

with open('NFA.json') as f:
    nfa = json.load(f)
inp = input("Input: ")
result = simulate_nfa(nfa, inp)
print("ACCEPTAT" if result else "RESPINS")