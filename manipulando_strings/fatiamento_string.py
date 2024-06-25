name = 'Bruno Reche Albertini'
curso = 'Análise e Desenvolvimento de Sistemas'
profissao = 'Analista de Dados'

print(name[0])
print(name[:])
print(name[:5])
print(name[6:11])
print(name[12:])
print(name[6:])

# ----------- Strings múltiplas linhas -----------

mensagem = f"""
Olá mundo!
Meu nome é {name[:5]}, atualmente faço o curso de {curso}
e também estudo Python,
e eu quero ser um {profissao}!
"""
print(mensagem)
