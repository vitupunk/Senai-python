import os
os.system

soma=0
quantidade_de_numeros=0

while True:
    nota=float(input("digite uma nota "))
    quant_nts+=1
    if nota<0:
        break
    else:
        soma<-nota
        media=soma/quant_nts

print(f"\media:{media}")