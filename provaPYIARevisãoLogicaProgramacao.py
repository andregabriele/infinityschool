usuario_correto ='andre'
senha_correta = '12345'

for tentativa in range(3):
    usuario = input('Digite o nome do usuário: ')
    senha = input('Digite a senha: ')

    if usuario == usuario_correto and senha == senha_correta:
        print('Bem vindo!')
        break
    elif tentativa < 2:
        print(f'Falta(m) {2 - tentativa} tentativa(s).')
else:
    for _ in range(3):
        print('Acesso bloqueado.')

