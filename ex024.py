cidade = input('Digite o nome de uma cidade: ')
cidade_split = cidade.split()
if cidade_split[0] == 'Santo' or cidade_split[0] == 'santo':
    print(f'A cidade {cidade} começa com Santo!')
else:
    print(f'A cidade {cidade} não começa com Santo!')
