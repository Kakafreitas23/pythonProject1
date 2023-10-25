


#• Certifique-se de que sua comparação não levará em conta as diferenças
#entre letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá
#ser aceito.

current_users=["Alberto","Julio","Ana","Melissa","Rodolfo"]
new_users=["Fábio","Michel","Patrick","Júlia","Samantha"]
current_users.append(new_users[0])
current_users.append(new_users[3])

for n in new_users:
    current_users = ["Alberto", "Julio", "Ana", "Melissa", "Rodolfo".lower()]
    new_users = ["Fábio", "Michel", "Patrick", "Júlia", "Samantha".lower()]
    current_users.append(new_users[0])
    current_users.append(new_users[3])
    if "Fábio"  and "Júlia" in new_users:
        print("A pessoa deverá fornecer um  novo nome")
    else:
        print("nome do usuário está disponível.")