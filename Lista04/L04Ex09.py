cont=1
voto1=0
voto2=0
voto3=0
voto4=0
voto5=0
voto6=0
voto7=0
voto8=0
voto9=0
voto10=0
while cont<=35:
    print('Vote 1 para Metal Gear Solid\nVote 2 para Driver\nVote 3 para Crash Bandicoot\nVote 4 para Warped\nVote 5 para Tekken 3\nVote 6 para Cortex Strikes Back\nVote 7 para Final Fantasy VIII\nVote 8 para Gran Turismo 2\nVote 9 para Final Fantasy VII')
    voto=int(input())
    if(voto==1):
        voto1=voto1+1
    if(voto==2):
        voto2=voto2+1
    if(voto==3):
        voto3=voto3+1
    if(voto==4):
        voto4=voto4+1
    if(voto==5):
       voto5=voto5+1
    if(voto==6):
       voto6=voto6+1
    if(voto==7):
       voto7=voto7+1
    if(voto==8):
       voto8=voto8+1
    if(voto==9):
       voto9=voto9+1
    if(voto<1):
        print('Voto anulado')
    if(voto>9):
        print('Voto anulado')
    cont+=1
if(voto1>voto2) and (voto1>voto3) and (voto1>voto4) and (voto1>voto5) and (voto1>voto6) and (voto1>voto7) and (voto1>voto8) and (voto1>voto9):
    print('Metal Gear Solid ganhou com ' , voto1, 'votos')
if(voto2>voto1) and (voto2>voto3) and (voto2>voto4) and (voto2>voto5) and (voto2>voto6) and (voto2>voto7) and (voto2>voto8) and (voto2>voto9):
    print('Driver ganhou com ' ,voto2, 'votos')
if(voto3>voto1) and (voto3>voto2) and (voto3>voto4) and (voto3>voto5) and (voto3>voto6) and (voto3>voto7) and (voto3>voto8) and (voto3>voto9):
    print('Crash bandicoot ganhou com ' , voto3, 'votos')
if(voto4>voto1) and (voto4>voto2) and (voto4>voto3) and (voto4>voto5) and (voto4>voto6) and (voto4>voto7) and (voto4>voto8) and (voto4>voto9):
    print('Warped ganhou com ' , voto4, 'votos')
if(voto5>voto1) and (voto5>voto2) and (voto5>voto4) and (voto5>voto3) and (voto5>voto6) and (voto5>voto7) and (voto5>voto8) and (voto5>voto9):
    print('Tekken 3 ganhou com ' , voto5, 'votos')
if(voto6>voto1) and (voto6>voto2) and (voto6>voto4) and (voto6>voto5) and (voto6>voto3) and (voto6>voto7) and (voto6>voto8) and (voto6>voto9):
    print('Tekken ganhou com ' , voto6, 'votos')
if(voto7>voto1) and (voto7>voto2) and (voto7>voto4) and (voto7>voto5) and (voto7>voto3) and (voto7>voto6) and (voto7>voto8) and (voto7>voto9):
    print('Tekken ganhou com ' , voto7, 'votos')
if(voto8>voto1) and (voto8>voto2) and (voto8>voto4) and (voto8>voto5) and (voto8>voto3) and (voto8>voto6) and (voto8>voto7) and (voto8>voto9):
    print('Final Fantasy VIII ganhou com ' , voto8, 'votos')
if(voto9>voto1) and (voto9>voto2) and (voto9>voto4) and (voto9>voto5) and (voto9>voto3) and (voto9>voto6) and (voto9>voto8) and (voto9>voto7):
    print('Final Fantasy VII 2 ganhou com ' , voto9, 'votos')

