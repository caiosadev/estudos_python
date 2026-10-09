usuarios = {
    'jessica' : {
        'nome' : 'Jéssica Araújo',
        'idade' : 35,
        'empresa' : 'Google',
        'usuario' : 'jaraujo',
        },
    'carlos' : {
        'nome' : 'Carlos Vasconcelos',
        'idade' : 47,
        'empresa' : 'V4 Company',
        'usuario' : 'cvasconcelos',
    },
    'eduardo' : {
        'nome' : 'Eduardo Borges',
        'idade' : 27,
        'empresa' : 'Microsoft',
        'usuario' : 'eborges',
    },
    'vanessa' : {
        'nome' : 'Vanessa de Souza',
        'idade' : 23,
        'empresa' : 'Meta',
        'usuario' : 'vsouza',
    },
}

for chaves, dados in usuarios.items():
    print(f"O usuário {dados['usuario']}, pertence a(o) {dados['nome']}, " 
          f"que trabalha na empresa {dados['empresa']}.\n")
