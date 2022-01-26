# 2.uzdevums. Lietotājs ievada kvadrāta malas garumu centimetros (>5cm).<br> Sastādīt programmas kodu, kas aprēķina, par cik procentiem mainīsies kvadrāta laukums, ja tā malas garums tiek mainīts par 5cm.<br> Atbildi izvadīt veselos procentos.
"""mala=float(input("ievadi malas garumu cm (>5cm): "))
laukums1=mala*mala
laukums2=(mala+5)*(mala+5)
print(f"laukums sākumā ir {laukums1} cm^2")
print(f"laukums pēc tam ir {laukums2} cm^2")
izmainas=laukums2*100/laukums1
print(f"laukums izmainās par {izmainas} %")"""

#papilduzdevums
import math
r=float(input("ievadi riņķa rādiusu: "))
hip=float(input("ievadi vienādsānu taisnleņķa trijstūra hipotenūzas garumu centimetros: "))
S_rinkim=math.pi*math.pow(r,2)
print(f"riņķa laukums {S_rinkim} cm")
S_trissturim=hip*(hip/2)/2
print(f"trisstūra laukums {S_trissturim} cm")
starpiba=S_rinkim-S_trissturim
print(f"riņķa laukums ir lielāks nekā trijstūra laukums par {round(starpiba,1)} cm")