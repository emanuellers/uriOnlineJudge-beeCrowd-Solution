#1134 - Tipo de Combustível
#Emanuelle Rodrigues
gaso = 0
alcool = 0
diesel = 0

while True:
    entrada = int (input ())
    if entrada == 4:
        break
    elif entrada == 1:
        alcool += 1
    elif entrada == 2:
        gaso += 1
    elif  entrada == 3:
        diesel += 1

print ("MUITO OBRIGADO")
print  ("Alcool: %d" %(alcool))
print ("Gasolina: %d"%(gaso))
print ("Diesel: %d" %(diesel))
        