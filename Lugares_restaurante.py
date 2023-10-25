# 7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
# quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que
# oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
# contrário, informe que sua mesa está pronta.

pergunta=int(input("Quantas pessoas estão convidadas para jantar ?"))
if pergunta>8:
    print("Deverão esperar uma mesa para jantar!")
else:
    print("A mesa está pronta!")