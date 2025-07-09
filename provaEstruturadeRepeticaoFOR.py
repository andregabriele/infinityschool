inicio_intervalo = int(input("Digite o número inicial do intervalo: "))
fim_intervalo = int(input("Digite o número final do intervalo: "))

soma_pares = 0
encontrou_par = False

for numero in range(inicio_intervalo, fim_intervalo + 1):
    if numero % 2 == 0:
        soma_pares += numero
        encontrou_par = True
else:
    if encontrou_par:
        print(f"A soma dos números pares no intervalo é: {soma_pares}")
    else:
        print("Não há números pares no intervalo.")
