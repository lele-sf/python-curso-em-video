nome = input('Digite o seu nome completo: ')
nome_upper = nome.upper()
nome_lower = nome.lower()
nome_length = len(nome.replace(' ',''))
nome_split = nome.split()
nome_fname = nome_split[0]

print(f'O seu nome em maiúsculas é: {nome_upper}')
print(f'O seu nome em minúsculas é: {nome_lower}')
print(f'Seu nome completo tem {nome_length} letras.')
print(f'Seu primeiro nome é {nome_fname} e tem {len(nome_fname)} letras.')
