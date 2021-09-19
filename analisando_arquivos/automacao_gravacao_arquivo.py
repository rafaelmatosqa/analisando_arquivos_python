fileName = input("Digite o nome do arquivo: ")
fileName = fileName + ".txt"
f3 = open("arquivos_novos/" + fileName, "w")
f3.write("Conteúdo novo incluido de forma automática")
f3.close()
f3 = open("arquivos_novos/" + fileName, "r")
print(f3.read())
f3.close()
