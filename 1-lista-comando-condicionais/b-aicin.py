food = input()
response = 'Opa! Parece que voce procura um tipo de comida que nao combina com essa epoca, tente novamente.'

if food == 'Canjica':
    response = 'Boa! Canjica faz parte.'
elif food == 'Pamonha':
    response = 'Boa! Pamonha faz parte.'
elif food == 'Bolo de milho':
    response = 'Boa! Bolo de milho faz parte.'

print(response)
