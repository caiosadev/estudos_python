linguagens_favoritas = {
    'ana' : 'python',
    'bruno' : 'java',
    'clara' : 'python',
    'eduardo' : 'c#',
}

print("Linguagens favoritas:")
#set() é usado para eliminar valores duplicados
for linguagem in set(linguagens_favoritas.values()):
    print(linguagem.title())
