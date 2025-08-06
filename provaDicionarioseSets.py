

nome = input("Digite seu nome completo: ").strip()
email = input("Digite seu email ").strip()

while True:
    telefone = input("Digite seu número do telefone (com DDD): ").strip()
    
    telefone_limpo = ''.join(filter(str.isdigit, telefone))
    
    if len(telefone_limpo) >= 10:
        break
    else:
        print("Telefone inválido. Digite com DDD e pelo menos 10 dígitos (ex: (11) 99999-8888)")


valores = set([nome, telefone, email])

contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email
}

print("Nome:", contato["nome"])
print("Telefone:", contato["telefone"])
print("Email:", contato["email"])