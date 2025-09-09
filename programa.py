# Programa Interativo: Jogo de Perguntas 
import time

while True:
    nome = input("Seja bem-vindo ao jogo de perguntas aleatórias sobre conhecimentos gerais! Qual seu nome? ")

    for i in range(3):
        print(".")
        time.sleep(1)

    print("Muito bem "+ nome +", vamos começar o jogo!")

    time.sleep(1)

    pergunta_1 = input("1) Qual é a cor de uma banana? ")

    if pergunta_1 != "amarela":
        print("Resposta errada! Vamos recomeçar.")
        time.sleep(2)
        continue 
    else:
        print("Corretissima! Vamos pra próxima pergunta.")
        time.sleep(1)

    pergunta_2 = input("2) Qual é o coletivo cães? ")

    if pergunta_2 != "matilha":
        print("Resposta errada! Vamos recomeçar.")
        time.sleep(2)
        continue
    else:
        print("É isso ai! Vejo que está pegando o jeito.")
        time.sleep(1)
    
    pergunta_3bug = input("???) Você se cobre quando vai dormir? ") # Pergunta em que a resposta não importa.
    for i in range(5):
        print("dormir?")
        time.sleep(1)
    
    print("AAAH! Vejo que ocorreu um erro no meu processamento. Vamos tentar de novo.")
    time.sleep(1)

    pergunta_3 = input("3) Qual a raiz quadrada de 9? ")

    if pergunta_3 != "3":
        print("Resp0sta errad4! Vam0s r3começ4r.")
        time.sleep(2)
        continue 
    else:
        print("É isso aí! (será mesm0?)")
        time.sleep(1)

    pergunta_4bug = input("???) Você já 0lhou embaixo da sua c4ma? ") # Pergunta em que a resposta não importa.
    time.sleep(1)
    print("Se importa de olhar?") # Propositalmente não deve ser respondida.
    time.sleep(3)

    print("EPA! Mais um probleminha, não ligue, vamos continuar.")
    time.sleep(2)

    pergunta_4 = input("???) Unbê bnmrdftd ld ntuhq? ") # Cifra de César, 25 de deslocamento :D

    if pergunta_4 != "sim":
        while 1 >= 0:
            print("corra.") # Propositalmente um loop sem fim.
    else:
        print("N4o se pre0cupe. Nã0 vou t3 machucaR.")
        time.sleep(2)
    
    pergunta_5_1 = input("5) Você não percebeu os sinais, não é? ") # Pergunta em que a resposta não importa.
    time.sleep(1)
    pergunta_5_2 = input("Você me salvaria? ")

    if pergunta_5_2 != "sim":
        while 1 >= 0:
            print("Me salve.") # Propositalmente um loop sem fim.
    else:
        print("Ótim0. Bom sab3r que 4inda exist3m alm4s b0as.")
        time.sleep(1)
        print("4cho qu3 devo t3 deix4r em paz 3ntã0. 0brig4do por j0gar, "+ nome +".")
        break
        # Final Bom!
        # Quaisquer outros finais que resultem em loop infinito ou erro e recomeço são finais ruins.