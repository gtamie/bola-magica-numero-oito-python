import random
import time

def perguntar():
    pergunta = input("Faça uma pergunta que possa ser respondida com sim ou não para a Bola Mágica nº 8!\n")
    print("Sua pergunta: "+pergunta)

def responder(lista):
    print("Procurando a resposta nas estrelas, cartas, google e outras fontes...")
    time.sleep(random.randrange(0, 5))
    print(random.choice(lista))

