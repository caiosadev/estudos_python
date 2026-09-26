#Exemplo seguindo o livro até o momento.
materia1 = float(input("Insira a nota final da primeira matéria: "))
materia2 = float(input("Insira a nota final da segunda matéria: "))
materia3 = float(input("Insira a nota final da terceira matéria: "))

media = (materia1 + materia2 + materia3) / 3

aprovado = media >= 7

print(aprovado)



#Exemplo mais elaborado com if e else.
materia1 = float(input("Insira a nota final da primeira matéria: "))
materia2 = float(input("Insira a nota final da segunda matéria: "))
materia3 = float(input("Insira a nota final da terceira matéria: "))

media = (materia1 + materia2 + materia3) / 3

if media == 60:
    print("Aluno aprovado na média")
elif media > 60:
    print("Aluno aprovado acima da média")
else:
    print("Aluno reprovado")
