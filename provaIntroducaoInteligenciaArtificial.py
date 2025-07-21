num_alunos = int(input("Digite o número de alunos: "))
soma_medias = 0

for i in range(num_alunos):
    print(f"Aluno {i + 1}:")
    nome = input("Nome do aluno: ")

    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    nota3 = float(input("Digite a 3ª nota: "))

    media = (nota1 + nota2 + nota3) / 3
    soma_medias += media

    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"

    print(f"Resultado do aluno: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")

media_geral = soma_medias / num_alunos
print(f"Média geral da turma: {media_geral:.2f}")
