mediaAluno = float(input("Informe a média do estudante: "))

if mediaAluno>=6.0:
    print("O aluno está aprovado!")
elif mediaAluno>4.0 and mediaAluno<=5.9:
    print("O aluno está de recuperação!")
else:
    print("O aluno foi reprovado!")