idade = int(input())

anos = int(idade/365)
meses = int((idade%365)/30)
dias = (idade%365)%30

print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")
