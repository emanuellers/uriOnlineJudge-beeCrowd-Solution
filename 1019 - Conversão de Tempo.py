#1019 - Conversão de Tempo
#Emanuelle Rodrigues
seg =int (input ())
hora = seg / 3600
minutos = (seg % 3600 ) / 60
sec = seg % 60
print ("%d:" %hora + "%d:" %minutos + "%d" %sec)