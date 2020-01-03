#1192 - O jogo Matemático de Paula
#Emanuelle Rodrigues
casos_teste = int(input())
for i in range(casos_teste):
    digitos  = str(input())
    num_1 = int(digitos[0])
    letra = digitos[1]
    num_2 = int(digitos[2])
    m_m = letra.lower()
    if num_1 == num_2:
        resultado = num_1 * num_2
    elif letra == m_m:
        resultado = num_1 + num_2
    else:
        resultado = num_2 - num_1
    print(resultado)
        