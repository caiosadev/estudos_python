#não entendi 100% a lógica dos cálculos desse exercício, porém foi possível finalizar

cigarros_dia = int(input("Quanto cigarros fuma por dia? "))
anos_consumo = int(input("Fuma há quantos anos? "))

conversao_ano = anos_consumo * 365 #conversão de anos em dias fumando
tempo_cigarro_dia = cigarros_dia * 10 #quantidade de minutos por cigarro

dia_minuto = 24 * 60 #conversao de 24 (1 dia) em minutos
dias_perdidos = conversao_ano * tempo_cigarro_dia / dia_minuto #quantos dias perdeu
conversao_dias_perdidos_minutos = dias_perdidos * dia_minuto #dias para minutos

#quantidade de cigarros fumados ao longo da vida
total_cigarros_consumidos = cigarros_dia * anos_consumo * 365 

print("Você fumou {} cigarros" .format(total_cigarros_consumidos))
print("Você perdeu {:.2f} dias de vida, equivalentes à {} minutos"
      .format(dias_perdidos, conversao_dias_perdidos_minutos))
