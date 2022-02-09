nome = [str(x) for x in input().split()]

for i in range(1, len(nome) - 1):
    if len(nome[i]) > 3:
        nome.insert(i, (nome[i])[0] + '.')
        nome.pop(i+1)

nome_abrev = " ".join(nome)

print(nome_abrev)  
                
