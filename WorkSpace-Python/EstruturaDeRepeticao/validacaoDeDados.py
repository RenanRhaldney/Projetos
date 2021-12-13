while True:
    nome = input('Nome: ').capitalize()
    idade = int(input('Idade: '))
    salario = float(input('Salario: '))
    sexo = input('Sexo: ').capitalize()
    estadoCivil = input('Estado civil: ').capitalize()
    
    if len(nome) <= 3:
        print('O nome precisa ser no minimo 4 characteres.')
    elif idade <= 0 or idade > 150:
        print('Idade invalida.')
    elif salario <= 0:
        print('Salario invalido.')
    elif sexo[0] != 'F' and sexo[0] != 'M':
        print('Sexo invalido. ')
    elif estadoCivil[0] != 'S' and estadoCivil[0] != 'C' and estadoCivil[0] != 'V' and estadoCivil != 'D':
        print('Estado civil invalido. ')
    else:
        print(f'\nDados corretos.\n'
              f'Nome: {nome}\n'
              f'Idade: {idade}\n'
              f'Salario: {salario:.2f}\n'
              f'Sexo: {sexo}\n'
              f'Estado civil: {estadoCivil}')
        break

print("FIM...")