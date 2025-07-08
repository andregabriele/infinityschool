right_answer = 7
tries = 3

while tries > 0:
    user_input = input("Qual é o número inteiro sorteado? Digite tentar adivinhar: ")
    
    i = 0
    if user_input == '':
        valido = False
    else:
        if user_input[0] == '-':
            i = 1  
        valido = i < len(user_input)
        while i < len(user_input):
            if user_input[i] < '0' or user_input[i] > '9':
                valido = False
                break
            i += 1

    if not valido:
        print("Esse não é um valor inteiro! Tente novamente.")
        continue

    
    answer = int(user_input)

    if answer == right_answer:
        print("Parabéns, você acertou!! Me diga o numero da mega-sena por favor.. rsrsrs!!")
        break
    else:
        tries -= 1
        if tries > 0:
            print(f"Errou! Tente novamente!! Restam {tries} tentativas!")
        else:
            print("Infelizmente acabaram as tentativas.. Volte amanhã!!")

