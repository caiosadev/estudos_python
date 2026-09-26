#mais simples igual ao livro
distancia = float(input("Qual a distância da viagem em KM? "))
velocidade_media_hora = float(input("Qual a velocidade média (por hora) no trajeto? "))

tempo_viagem = distancia / velocidade_media_hora

print("O tempo estimado da viagem é: {:.2f} horas" .format(tempo_viagem))



#mais elaborado
distancia = float(input("Qual a distância da viagem em KM? "))
velocidade_media_hora = float(input("Qual a velocidade média (por hora) no trajeto? ")) #horas
pedagios = int(input("Quantos pedágios no caminho? "))
tempo_pedagios = int(input("Quanto tempo aproximado em cada pedágio, em minutos? ")) #minutos

# *60 para converter em minutos
tempo_viagem = ((distancia / velocidade_media_hora) * 60) + (pedagios * tempo_pedagios) 
tempo_horas = (tempo_viagem // 60) #converte para horas inteiras, sem sobras
tempo_minutos = (tempo_viagem % 60) #converte as sobras para minutos
#tempo_minutos = tempo_viagem - 60 #também funciona para transformar os minutos

print("O tempo estimado da viagem é de: {:.0f} minutos, equivalente a {:.0f}h e {:.0f}m"
      .format(tempo_viagem, tempo_horas, tempo_minutos))