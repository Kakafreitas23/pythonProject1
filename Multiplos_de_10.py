# 7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
# # número é múltiplo de dez ou não.

numero_do_usuario=int(input("Digite um número : "))
multiplo=(numero_do_usuario%10)==0
if multiplo:
    print("O número {} é multiplo de 10 ".format(numero_do_usuario))
else:
    print("O número {} não é multiplo de 10".format(numero_do_usuario))