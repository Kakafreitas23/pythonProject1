# 7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
# fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
# fornecido. À medida que cada ingrediente é especificado, apresente uma
# # mensagem informando que você acrescentará esse ingrediente à pizza.

ingredientes=True
while ingredientes:
    escolha=str(input("Qual será o ingrediente?"))
    if escolha=="Quit":
        break
    else:
        print("Ingrediente adicionado á pizza")


