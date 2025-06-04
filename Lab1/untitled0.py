def verify(a):
    n=len(a[0])
    for line in a:
        if n!=len(line):
            print("Eroare!")
            return 0
    return 1
    

def save_matrix(a,fn1):
    a=load_matrix("matrice.in")
    fout=open(fn1,'w')
    if verify(a):
        for line in a:
            fout.write(" ".join(map(str,line))+"\n")
        
    

def load_matrix(fn):
    fin=open(fn,'r')
    lines=fin.readlines()
    a=[[int(x) for x in line.strip().split()]for line in lines if line[0]!="#"]
    return a


a=[]
save_matrix(a,"matrice.out")
            
    