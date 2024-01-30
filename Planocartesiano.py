print('Plano Cartersiano X,Y')

Cordenadas_x = int(input('Insira as Cordenadas X:'))
Cordenadas_y = int(input('Insira as Cordenadas Y:'))

if Cordenadas_x > 0 and Cordenadas_y > 0:
    print('Primeiro Quadrante')
elif Cordenadas_x < 0 and Cordenadas_y > 0:
    print('Segundo Quadrante')
elif Cordenadas_x < 0 and Cordenadas_y < 0:
    print('terceiro quadrante')
elif Cordenadas_x > 0 and Cordenadas_y < 0:
    print('Quarto quadrante')
else:
    print('Eixo de origem')
