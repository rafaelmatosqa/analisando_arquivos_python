# Lendo arquivo

# Abrir um arquivo para leitura

f1 = open("arquivos/arquivo1.txt", "r")

# Lendo o arquivo
print(f1.read())

# Contar o número de caracteres
print(f1.tell())

# Retornar para o inicio do arquivo
print(f1.seek(0, 0))

# Ler os primeiros 10 caracteres do arquivo
print(f1.read(10))

# Escrevendo no arquivo

# Abrindo o arquivo
f2 = open("arquivos/arquivo1.txt", "w")
# Escrevendo no arquivo
print(f2.write("Novo conteúdo adicionado no arquivo1"))
# Fechando o arquivo
print(f2.close())

# Abrindo o arquivo para leitura
f2 = open("arquivos/arquivo1.txt", "r")
# Escrevendo no arquivo
print(f2.read())
# Fechando o arquivo
print(f2.close())

# Adicionando conteudo a um arquivo sem apagar o conteúdo existente
f2 = open("arquivos/arquivo1.txt", "a")
print(f2.write(" Incluindo mais conteúdo no arquivo"))
# Fechando o arquivo
print(f2.close())

# Lendo arquivo com novo conteudo incluído
f2 = open("arquivos/arquivo1.txt", "r")
print(f2.read())
# Fechando o arquivo
print(f2.close())
