#El programa quiere poder contar cuantas
# de una letra tiene la cadena que ha metido el usuario,
# después de sacar el número de letras sacara por pantalla
# los 4 últimos caracteres(tener cuidado de que no meta espacios en blanco).
per = (str(input("Ingresa el nombre" + '\n')))
per = per.strip()
try:
    lett=(str(input("Ingresa la letra solo 1" + '\n')))
    lett.strip()
    lett=lett[0]
except:
    print("Solo 1 letra")
cont=0
for c in per:
    if(c==lett.lower() or c==lett.upper()):
        cont+=1
print("La letra "+str(lett)+" sale: "+str(cont)+" veces")
ult:int=len(per)-3
print(str(per[ult:]))


#kaishclcjashcdascjashc
#ksdhckajhcajghcaj