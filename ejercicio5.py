valor_n = int(input("Ingresa un número N "))
while valor_n< 3:
    valor_n = int(input("N tiene que ser mayor o igual a 3. Ingresa N nuevamente: "))
matriz = [[0]*valor_n for _ in range(valor_n)]
num = 1
inicio_fila = 0
fin_fila = valor_n - 1
inicio_col = 0
fin_col = valor_n - 1
while num <= valor_n*valor_n:
    for col in range(inicio_col, fin_col + 1):
        matriz[inicio_fila][col] = num
        num += 1
    inicio_fila += 1

    for fila in range(inicio_fila, fin_fila + 1):
        matriz[fila][fin_col] = num
        num += 1
    fin_col -= 1

    for col in range(fin_col, inicio_col - 1, -1):
        matriz[fin_fila][col] = num
        num += 1
    fin_fila -= 1

    for fila in range(fin_fila, inicio_fila - 1, -1):
        matriz[fila][inicio_col] = num
        num += 1
    inicio_col += 1
for fila in matriz:
    print(fila)
