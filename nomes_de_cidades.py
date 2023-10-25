# 8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
# aceite o nome de uma cidade e seu país. A função deve devolver uma string
# formatada assim: "Santiago, Chile"
# Chame sua função com pelo menos três pares cidade-país e apresente o valor
# devolvido.

def city_country(nome_cidade,nome_país):
    nome=nome_cidade+nome_país
    return nome
nomes=city_country("Santiago, ","Chile")
print(nomes)

# while True:
# def city_country2(nome_cidade,nome_país,nome_cidade1,nome_país1,nome_cidade2,nome_país2):
#     nome_0=nome_cidade+nome_país+nome_cidade1+nome_país1+nome_cidade2+nome_país2)
#     return nome_0
#     nomes_cidade_país=city_country2("Santiago","Chile","Rio de Janeiro","Brasil","Berlim","Alemanha")
#     print(nomes_cidade_país)
#
#
#
