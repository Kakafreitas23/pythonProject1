# Sanduíches: Escreva uma função que aceite uma lista de itens que uma
# pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe
# tantos itens quantos forem fornecidos pela chamada da função e deve
# apresentar um resumo do sanduíche pedido. Chame a função três vezes usando
# um número diferente de argumentos a cada vez.

def sanduiches(*itens):
    """Lista de Itens"""
    print(itens)
sanduiches("Frango")
print("Sanduiche de Frango contém :Pão,frango,salada,milho e ervilha.\n")
sanduiches("Carne")
print("Sanduiche de Carne contém :Pão,Carne,Presunto e Salada.\n")
sanduiches("Peixe")
print("Sanduiche de Peixe contém :Pão,Peixe e Molho.")
