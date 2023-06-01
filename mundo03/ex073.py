times = ('Botafogo','Palmeiras','São Paulo','Atlético-MG','Grêmio','Cruzeiro','Flamengo','Fluminense','Fortaleza','Bragantino','Athletico-PR','Santos','Internacional','Corinthians','Cuiabá','Bahia','Goiás','Vasco','América-MG','Coritiba')

print(f'Lista de times do Brasileirão: {times}')
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Vasco está na {times.index("Vasco")+1}° posição')