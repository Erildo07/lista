frase = 'Olá, tudo bem?'
print(str.lower(frase))  # Converte a frase para minúsculas

# Separando a frase em uma lista usando ',' como delimitador
frase_separada = frase.split(',')
print(frase_separada[1])  # Exibe o segundo elemento da lista após a separação

lista_nomes = ['SSH', 'Erildo Nunes', 'João', 'Maria', 'Lorena', 'Ghost', 'SSH']

# Adicionando elementos à lista
lista_nomes.append('Julio')
lista_nomes.append('Juliana')
lista_nomes.append('SSH')

# Removendo um elemento específico da lista
lista_nomes.remove('João')

# Contando o número de ocorrências de 'SSH'
contador_SSH = lista_nomes.count('SSH')

# Exibindo a lista e o contador de 'SSH'
print(lista_nomes)
print(contador_SSH)

# Exibindo o comprimento da lista
print(len(lista_nomes))

# Removendo e exibindo os dois últimos elementos da lista
print(lista_nomes.pop())
print(lista_nomes.pop())

# Exibindo a lista final após os elementos removidos
print(lista_nomes)
