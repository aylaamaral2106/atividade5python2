aluno1 = input("Digite sua nota: ")
aluno2 = input("Digite sua nota: ")
aluno3 = input("Digite sua nota: ")
aluno4 = input("Digite sua nota: ")

minhalista = [aluno1, aluno2, aluno3, aluno4,]
minhalista.sort()

soma = float(aluno1) + float(aluno2) + float(aluno3) + float(aluno4)
media = float(soma/4)

notasformatado = str(minhalista) + " foram as notas e a media é de " + str(media)

print(notasformatado)
