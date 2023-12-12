# Faça um programa que solicite ao usuário que digite 10 valores para
# preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes.
# Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e
# ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.


valores = []
pares = []
impares = []
for i in range(10):
    numero = int(input(f'Digite {i+1}º número: '))
    valores.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

tupla_pares = tuple(pares)
print(f'Números pares: {tupla_pares}')
tupla_impares = tuple(impares)
print(f'Números ímpares: {tupla_impares}')
print(f'Quantidade de números pares: {len(tupla_pares)}')
print(f'Quantidade de números ímpares: {len(tupla_impares)}')
print(f'Somatório dos números pares: {sum(pares)}')
print(f'Somatório dos números ímpares: {sum(impares)}')
