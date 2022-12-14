# José Daniel Fernández López
# 2022-12-14
def contarpalabras(texto):
    texto = texto.lower()
    texto = texto.split(" ")
    frecuencia_palabras = {}
    for palabra in texto:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra]+=1
        else:
            frecuencia_palabras[palabra]=1
    return frecuencia_palabras

mi_string = input("Introduce texto: ")
conteo_palabras = contarpalabras(mi_string)
mas_de_una = []
for palabra in conteo_palabras:
    if conteo_palabras[palabra] > 1:
        mas_de_una.append(palabra)
print(conteo_palabras)
print(mas_de_una)
