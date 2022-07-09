day = int(input())
response = 'Você escolheu um dia que não irá acontecer nenhum show, tente novamente!'

if day != 20 and 17 <= day <= 26:
    if day % 2 == 0:
        response = 'Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!'
    else:
        response = 'Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!'

print(response)
