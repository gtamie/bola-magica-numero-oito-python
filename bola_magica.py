from funcoes_bola_magica.funcoes_bola_magica import *

# algumas respostas originais da bola foram substituídas para melhor adaptação ao português
respostas = ["Com certeza", "Pode apostar que sim", "Definitivamente sim", "Sem dúvida", "Pode confiar que sim",
             "A meu ver, sim", "Muito provavelmente", "Parece que sim", "Sim", "Os sinais apontam que sim",
             "Pergunte novamente mais tarde", "Melhor não te responder agora", "Não é possível prever agora",
             "Concentre-se e pergunte novamente", "A resposta que você procura não está aqui",
             "Não conte com isso", "Minha resposta é não", "Minhas fontes dizem que não", "Parece que não",
             "Duvido"
             ]

perguntar()
responder(respostas)

while True:
    continuar = input("Você gostaria de fazer outra pergunta? Digite S para continuar ou N para encerrar: ").upper()
    #se o usuário reponder qualquer coisa diferente de S, o programa encerra
    if not(continuar == "S"):
        print("Volte se tiver mais perguntas!")
        break
    perguntar()
    responder(respostas)