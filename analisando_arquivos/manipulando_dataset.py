# Abrindo um dataset em uma única linha
f = open("arquivos/salarios.csv", "r")
data = f.read()
rows = data.split('\n')
print(rows)

# Dividindo um dataset em colunas
f = open("arquivos/salarios.csv", "r")
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

print(full_data)

# Calculando o total de linhas do arquivo e imprimindo resultado
f = open("arquivos/salarios.csv", "r")
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

count = 0
for row in full_data:
    count += 1

print(count)

# Contando o número de colunas de um arquivo
f = open("arquivos/salarios.csv", "r")
data = f.read()
rows = data.split('\n')
full_data = []
for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]

count = 0
for column in first_row:
    count = count + 1

print(count)
