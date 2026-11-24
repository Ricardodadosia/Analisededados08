produto1 = {} # dicionario vazio 

produto = {
    'nome': 'notebook',
    'preço': 3500.80,
    'marca': 'lenovo'
}

print(produto) #todas as chaves e valores 

print(produto{'nome'}) 
print(produto{'preco'}) 

# Alterando o valor
produto['marca'] = "positivo"
print(produto{'marca'}) 

# Adicionando Chaves
produto['tela'] = '18"'
print(produto)

# deletando uma chave 
del produto['marca']
print(produto)

print(produto.keys()) #chaves
print(produto.values()) #valores 
print(produto.items()) #