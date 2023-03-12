# José Daniel Fernández López
# 2022-12-01
palabra1 = input("Introduce la primera palabra: ").upper()
palabra2 = input("Introduce la segunda palabra: ").upper()
lista_p1 = tuple(sorted(palabra1))
lista_p2 = tuple(sorted(palabra2))
# print(lista_p1)
# print(lista_p2)
def son_anagramas(lista_a, lista_b):
    if lista_a == lista_b:
        print("Las palabras son anagramas.")
    else:
        print("Las palabras no son anagramas.")
son_anagramas(lista_p1,lista_p2)