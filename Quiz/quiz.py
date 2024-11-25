print("Seja bem-vindo ao seu quiz!")
resposta_usuario = input ("Deseja continuar? (S/N) ")

if resposta_usuario != "S":
    quit()
    
score = 0

print("Começando... \n")

print("Qual é o maior oceano do mundo? \n (A) Oceano Atlântico \n (B) Oceano Índico \n (C) Oceano Ártico \n (D) Oceano Pacífico \n")
resposta_1 = input("Resposta: ")

if resposta_1 == "D":
    print("Correta! \n")
    score = score + 1
else:
    print("Incorreto! \n")
    
print("Quem pintou a Mona Lisa? \n (A) Vincent van Gogh \n (B) Leonardo da Vinci \n (C) Pablo Picasso \n (D) Michelangelo \n")
resposta_2 = input("Resposta: ")

if resposta_2 == "B":
    print("Correta! \n")
    score = score + 1
else:
    print("Incorreto! \n")
    
print("Qual é o país mais populoso do mundo? \n (A) Índia \n (B) Estados Unidos \n (C) Indonésia \n (D) China \n")
resposta_3 = input("Resposta: ")

if resposta_3 == "D":
    print("Correta! \n")
    score = score + 1
else:
    print("Incorreto! \n")
    
print("Qual é a fórmula química da água? \n (A) H2O \n (B) CO2 \n (C) NaCl \n (D) O2 \n")
resposta_4 = input("Resposta: ")

if resposta_4 == "A":
    print("Correta! \n")
    score = score + 1
else:
    print("Incorreto! \n")
    
print("Qual é o maior planeta do Sistema Solar? \n (A) Marte \n (B) Terra \n (C) Júpiter \n (D) Saturno \n")
resposta_5 = input("Resposta: ")

if resposta_5 == "C":
    print("Correta! \n")
    score = score + 1
else:
    print("Incorreto! \n")
    
print(f"O quiz acabou. Sua Pontuação é: {score}/5")
    

    

    
