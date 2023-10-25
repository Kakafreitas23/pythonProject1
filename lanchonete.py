# 7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com
# os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
# finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
# mostre uma mensagem para cada pedido, por exemplo, Preparei seu
# sanduíche de atum. À medida que cada sanduíche for preparado, transfira-o
# para a lista de sanduíches prontos. Depois que todos os sanduíches estiverem
# prontos, mostre uma mensagem que liste cada sanduíche preparado.

sandwich_orders=["Frango","Carne","Bacon","Atum"]
finished_sandwiches=[]
while sandwich_orders:
        print("Preparei o seu sanduiche de Frango")
        finished_sandwiches.append(sandwich_orders[0])
        print("Preparei o seu sanduiche de Carne")
        finished_sandwiches.append(sandwich_orders[1])
        print("Preparei o seu sanduiche de Bacon")
        finished_sandwiches.append(sandwich_orders[2])
        print("Preparei o seu sanduiche de Atum")
        finished_sandwiches.append(sandwich_orders[3])
        break
print(finished_sandwiches)