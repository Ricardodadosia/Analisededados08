# funções 


# defenindo uma função 
def saudacao():
    print('olá!')


def saudacao2(x):
    print(f'olá! {x}')

# saudacao()
# ---------------------------------------------------

nome = input('nome: ')
saudacao2(nome) # passagem por parametro 
saudacao2('antonio')
saudacao2('pedro')