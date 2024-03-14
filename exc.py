# print('Python na Escola de Programação da Alura')

# nome = 'luiz'
# idade = 17

# print(f'Meu nome é {nome} e tenho {idade} anos')

# print('A','L','U','R','A',sep='\n')



# pi = 3.14159

# print(f'O valor aproximado de pi é: {pi:.2f}')



# numero = int(input('Digite um número: '))

# if numero % 2:
#     print('seu numero é impar')
# else:
#     print('seu numero é par')



# idade = int(input('Digite sua idade: '))

# if idade <= 12:
#     print('Você é uma criança')
# elif idade <= 18:
#     print('Você é um adolecente')
# else:
#     print('Você é um adulto')



# nome = input('Digite seu nome: ')
# senha = input('Digite sua senha: ')
# nome_certo = 'luiz'
# senha_certa = 'royale'

# if nome == nome_certo and senha == senha_certa:
#     print('Você logou corretamente')
# else:
#     print('nome ou senha estão errados')



# cordx = int(input('digite a coordenada X: '))
# cordy = int(input('digite a coordenada Y: '))

# if cordx > 0 and cordy > 0:
#     print('Você está no primeiro quadrante')
# elif cordx < 0 and cordy > 0:
#     print('Você está no segunto quadrante')
# elif cordx < 0 and cordy < 0:
#     print('Você está no terceiro quadrante')
# elif cordx > 0 and cordy < 0:
#     print('Você está no quarto quadrante')
# else:
#     print('Você está na origem')


# numeros = [1,2,3,4,5,6,7,8,9,10]
# nomes = ['joão', 'pedro', 'lucas', 'erik']
# anos = ['2006', '2024']


# lista = ['urso', 'elefante', 'tigre', 'tucano']
# for animais in lista:
#     print(f'.{animais}')


# soma_impares = 0
# for i in range(1, 11, 2):
#     soma_impares += i
# print(soma_impares)


# for i in range(10, 0, -1):
#     print(i)


# numero = int(input('digite um número: '))
# for i in range(1, 11):
#     resultado = numero * i
#     print(f'{numero} x {i} = {resultado}')


# soma = 0
# numeros = [1,23,5,6,13,21]

# try:
#     for num in numeros:
#         soma += num
#     print(f'soma dos elementos: {soma}')
# except Exception as e:
#     print(f'ocorreu um erro: {e}')


# soma = 0
# lista = [1, 14, 56, 38, 29]

# try:
#     for i in lista:
#         soma += i
#         media = soma / len(lista)
#     print(f'a media é {media}')
# except zerodiv:
#     print('a lista tá vazia')
# except Exception as e:
#     print(f'ocorreu um erro: {e}')


# dic = [{'nome':'luiz', 'idade':17, 'cidade':'diadema'}]

# dic['cidade'] = 'são paulo'
# dic['profissão'] = 'programdor'
# del dic['idade']


# numeros_quadrados = {x: x**2 for x in range(1, 6)}
# print(numeros_quadrados)


# chave = [{'nome':'valeria', 'id':123}]
# if 'id' in chave:
#     print('achei')
# else:
#     print('não achei')


frase = 'tres pratos de trigo para tres tigres tristes'
contagem = {}
palavras = frase.split()
for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1
print(contagem)