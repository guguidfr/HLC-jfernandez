# José Daniel Fernández López
# 06/10/2022
n=int(input("Introduce un número (>1): "))
print(f"Los números pares hasta {n} son: ")
for i in range(2,n+1):
    print(i if i%2 == 0 else " ", end="")