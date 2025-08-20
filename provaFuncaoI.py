def media(num_1, num_2, num_3):
    return (num_1 + num_2 + num_3) / 3


try:
    numero_um = float(input('Digite o primeiro número: '))
    numero_dois = float(input('Digite o segundo número: '))
    numero_tres = float(input('Digite o terceiro número: '))

    resultado = media(numero_um, numero_dois, numero_tres)
    print(f'O valor da média aritmética calculada é: {resultado:.2f}')
except ValueError:
    print('Por favor, digite apenas números válidos.')
