# class restaurant:
#     def __init__(self,name,cuisine_type):
#         self.name=name
#         self.cuisine_type=cuisine_type
#
#     def describe_restaurant(self):
#         print(f"O nome do restaurante{self.name} e  a comida tipica é {self.cuisine_type}")
#
#     def open_restaurant(self):
#         print("O restaurante está aberto")
#
# restaurante=restaurant("Restaurante do Japa","Comida Japonesa")
# print(restaurante.name)
# print(restaurante.cuisine_type)
# restaurante.describe_restaurant()
# restaurante.open_restaurant()

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The name of the Restaurant is {} and it makes {}'.format(self.name, self.cuisine_type))
    def open_restaurant(self):
        print('The Restaurant is open')

restaurant=Restaurant('Chinese food', 'Hot Noodles')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()