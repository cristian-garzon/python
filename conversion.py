traductor={'hogar':'home','perro':'dog','barco':'boat','hermoso':'beautiful','mi':'my','es':'it´s','muy':'so'}
español=input("escribe la frase en español: ")
español = español.split(" ")
ingles=""
for i in español:
    if i in traductor:
        ingles+=traductor[i]+" "
    else:
        ingles+="(ERROR)"
print(ingles)