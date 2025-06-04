def load_automata(fn,fn2):
    fin=open(fn,'r')
    fout=open(fn2,'w')
    lines=fin.readlines()
    Q=[]
    S=[]
    A=[]
    for line in lines:
        line=line.strip()
        if line=='[States]':
            ok=1
        else:
            if line=='[End]' and ok==1:
                ok=0
                if len(S)>0:
                    fout.write(f"Starile intermediare sunt:{S}"+"\n")
            else:
                if ok==1:
                    q,s=line.split(',')
                    Q.append(q)
                    if s=='0':
                        fout.write(f"Starea initiala este:{q}"+"\n")
                    else:
                        if s=='1':
                            fout.write(f"Starea finala este:{q}"+"\n")
                        else:
                            if s!='1' or s!='0':
                                S.append(q)
                else:
                    if line=='[Sigma]':
                        ok=2
                    else:
                        if line=='[End]' and ok==2:
                            ok=0
                            A=sorted(A)
                            fout.write(f"Alfabetul este:{A}"+"\n")
                        else:
                            if ok==2:
                                a=line.split()
                                A.append(a)
                            else:
                                if line=='[Transitions]':
                                    ok=3
                                else:
                                    if line=='[End]' and ok==3:
                                        ok=0
                                    else:
                                        s1,t,s2=line.split(',')
                                        fout.write(f"{s1},{s2},{t}"+"\n")
                                        
                 

load_automata("automata.in","automata.out")