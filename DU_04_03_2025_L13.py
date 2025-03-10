class Pasta:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.topping = None
        self.dressing = None


    def __str__(self):
        return f'Pasta type: {self.type}, Sauce: {self.sauce}, Topping: {self.topping}, Dressing: {self.dressing},'


class PastaBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def set_type(self, type):
        self.pasta.type = type
        return self
    def set_sauce(self, sauce):
        self.pasta.sauce = sauce
        return self
    def set_topping(self, topping):
        self.pasta.topping = topping
        return self
    def set_dressing(self, dressing):
        self.pasta.dressing = dressing
        return self

    def build(self):
        return self.pasta

penne_cream = PastaBuilder().set_type("penne").set_topping("cream").build()
spaghetti_bolognese = PastaBuilder().set_type("spaghetti").set_topping("tomato").set_dressing("sour").build()
gnocchi_salmon=PastaBuilder().set_type("gnocchi").set_topping("salmon").set_sauce("hollandaise").build()
print('Displaying dish penne_cream:',penne_cream)
print('Displaying dish spaghetti_bolognese:',spaghetti_bolognese)
print('Displaying dish gnocchi_salmon:',gnocchi_salmon)