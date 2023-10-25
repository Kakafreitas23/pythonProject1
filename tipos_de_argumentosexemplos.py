# def describe_pet(animal_type,pet_name):
#     """Informações do animal"""
#     print("I have a "+animal_type)
#     print( "My " +animal_type, "name is " + pet_name)
# describe_pet("Hamster","Harry")
# describe_pet("Dog","Rodolfo")
# def describe_pizza(pizza_tamanho,pizza_sabor):
#     """Informaçoes da pizza"""
#     print("Eu quero uma pizza tamanho "+pizza_tamanho+" e sabor "+pizza_sabor)
#     # print("e sabor "+pizza_sabor)
# describe_pizza("Gigante","Calabresa")
#
#
# def describe_lugares(país,cidade):
#     print("Eu fui para o "+ país+ " e passeei na cidade de "+cidade)
# describe_lugares(país="Itália",cidade="Roma")


def describe_pet(pet_name,animal_type='dog'):
    """Exibe informações"""
    print("\nI have a " + animal_type + ".\n")

    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')