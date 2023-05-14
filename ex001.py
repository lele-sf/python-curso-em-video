name = input('Qual eh o seu nome? ')
name = name.title().strip()
firstName, lastName = name.split()
print(f'Bem vindo(a), {firstName}')