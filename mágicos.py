# 8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
# função chamada show_magicians() que exiba o nome de cada mágico da
# lista.


nomes=["Ari ","Roberto ","Arthur"]
def show_magicians(names):
    """Olá mágicos"""
    for m in names:
      msg=m.title()
      print(msg)
print("Os mágicos são: ")
show_magicians(nomes)


