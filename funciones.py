def palabras(texto):
    texto=texto.split()
    words={}
    for i in range(len(texto)):
        if texto[i] in words:
            words[texto[i]] += 1
        else:
            words[texto[i]]=1
    return words
def mas_usada(texto):
    mayor=0
    palabra=''
    for i,j in texto.items():
        if mayor<j:
            mayor=j
            palabra=i
    tupla=(mayor,palabra)
    return tupla

text='Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(palabras(text))
print(mas_usada(palabras(text)))