start_message = "Olá"

name_user = input("Qual o seu nome? ")
age_user = int(input("Qual a sua idade? "))
stature_user = float(input("Qual a sua altura? "))

print("{}, {}! Você têm {} anos e {:.2f} de altura."
      .format(start_message, name_user, age_user, stature_user))