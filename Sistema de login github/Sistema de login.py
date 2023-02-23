'''
Sistema de login
'''

while True:
    usuario_cadastrado = input('Cadastre um usuário com no máximo 8 caracteres: ')
    senha_cadastrada = input('Digite uma senha para cadastro com no máximo 8 digitos: ')
    qtd_letras = len(usuario_cadastrado)
    qtd_senha = len(senha_cadastrada)
    if qtd_letras >8:
       print('Tem que ser um usuário com no máximo 8 caracteres')
       continue
    elif qtd_letras <=4:
        print('Tem que ser um usuário com mais de 4 caracteres')
        continue
    elif qtd_senha <=4:
        print('Senha muito pequena')
        continue
    elif qtd_senha >8:
        print('Senha muito grande')
        continue
    else:
       print('Por favor, confirme seu cadastro!')
       break
while True:
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    if usuario_cadastrado == usuario and senha_cadastrada == senha:
        print('Usuário cadastrado, por favor faça o login.!')
        break
    else:
        print('Você precisa digitar um usuário válido')
        continue
while True:
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    if usuario == usuario_cadastrado and senha == senha_cadastrada:
       print('Usuario logado!')
       break
    else:
       print('Usuario ou senha inválido')
       continue
