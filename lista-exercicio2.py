soma_impares = 0
for numeros_im in range(1, 11, 2):
    print(numeros_im)
    
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

