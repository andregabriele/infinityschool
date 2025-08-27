def maior_numero(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2>= num3:
        return num2
    else:
        return num3


numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
numero_3 = float(input('Digite o terceiro número: '))

comparar_numeros = maior_numero(numero_1, numero_2, numero_3)
print(f'O maior numéro é: {comparar_numeros}')