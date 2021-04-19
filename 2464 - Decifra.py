alfabetoNormal = "abcdefghijklmnopqrstuvwxyz"
alfabetoNovo = input()
palavra = input()
novapalavra = ""
for i in palavra:
  letra = alfabetoNovo.index(i)
  letraNormal = alfabetoNormal[letra]
  novapalavra += letraNormal

print(novapalavra)


