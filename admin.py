nomes=["Alex","Henrique","João","Pedro","admin"]
nomes.remove("admin")
nomes.remove("Pedro")
nomes.remove("João")
nomes.remove("Henrique")
nomes.remove("Alex")

for n in nomes:
    print(n)
    if "Alex" in nomes:
        print("Bom dia Alex")
    if "Henrique" in nomes:
        print("Boa tarde Henrique" )
    if "João" in nomes:
        print("Boa noite Jõao")
    if "Pedro" in nomes:
        print("Good night Pedro")
    if "admin" in nomes:
        print("Olá admin, gostaria de ver um relatório de status?")
    if len(0) in nomes:
        print("Se a lista estiver vazia, mostre a mensagem Precisamos encontrar "
              "alguns usuários")
    else:
        print("Olá Erick")

