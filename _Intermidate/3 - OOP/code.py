class Chef:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name} Age: {self.age}")

    def cook_rice(self):
        print("Rice is available")

    def bake_cake(self):
        print("The cake is yummy")

class Nigeria_chef(Chef):
    def __init__(self, name, age, state_of_origin):
        super().__init__(name, age)
        self.state_of_origin = state_of_origin

    def cook_jollof(self):
        print("Jollof Rice sooo yummmy")

semi = Nigeria_chef('semi', 25, 'Lagos')
semi.show_details()
semi.cook_rice()
semi.bake_cake()
semi.cook_jollof()


# class Nigeria_chef:
#     def __init__(self, name, age, state_of_origin):
#         self.name = name
#         self.age = age
#         self.state_of_origin = state_of_origin
#
#     def cook_rice(self):
#         print("Rice is available")
#
#     def bake_cake(self):
#         print("The cake is yummy")
#
#     def cook_jollof(self):
#         print("Jollof Rice sooo yummmy")
