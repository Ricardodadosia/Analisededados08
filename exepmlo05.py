def soma(x, y):
    r = x + y 
    # print(r)
    return r 

# num1 = 5 
# num2 = 9 
# soma(num1, num2)
for i in range(3):
    num1 = float(input('informe o numero: '))
    num2 = float(input('informe outro numero: '))
    resultado = soma(num1, num2) # chamada da função 
    print(resultado)