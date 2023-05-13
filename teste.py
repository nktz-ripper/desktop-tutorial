nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
objetivo = input("Digite seu objetivo: ")
VIDAÚTIL = 60-int(idade)
print("Olá, ", nome)
print("Você tem ", VIDAÚTIL, "anos restantes na população economicamente ativa.")
print("") 
if VIDAÚTIL > 30:
  print("Se o seu objetivo é ",objetivo, ", você precisa se dedicar muito!")
else:
  print("Lamento, mas se o seu objetivo é ",objetivo, ", melhor não esquecer de dar alta prioridade a sua aposentadoria!")
print("Obrigado!")
