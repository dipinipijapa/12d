# 2.uzdevums. Lietotājs ievada kvadrāta malas garumu centimetros (>5cm).<br> Sastādīt programmas kodu, kas aprēķina, par cik procentiem mainīsies kvadrāta laukums, ja tā malas garums tiek mainīts par 5cm.<br> Atbildi izvadīt veselos procentos.
mala=float(input("ievadi malas garumu cm (>5cm): "))
laukums1=mala*mala
laukums2=(mala+5)*(mala+5)
print(f"laukums sākumā ir {laukums1} cm^2")
print(f"laukums pēc tam ir {laukums2} cm^2")
izmainas=laukums2*100/laukums1
print(f"laukums izmainās par {izmainas} %")


# 3.uzdevums Eksportē veiktās izmaiņas uz GitHub repozitoriju<br> Pārliecinies, ka risinājums ir redzams GitHub repozitorijā
