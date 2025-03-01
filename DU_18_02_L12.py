# class Country_city_pair:
#     def __init__(self, country, capital):
#         self.country=country
#         self.capital=capital
#
# sk=Country_city_pair
import pickle
class CountriesDict:
    def __init__(self):
        self.data={}

    def add_country(self, country, capital):
        self.data[country] = capital

    def view_contents(self):
        print(self.data)

    def delete_country(self, country):
        return self.data.pop(country, None)

    def find_country(self, country):
        if self.data.get(country)!=None:
            print('The country', country, 'is included and its capital is', self.data.get(country))
        else:
            print('The country', country, 'is not included')
    def edit_capital(self, country, capital):
        if self.data.get(country)!=None:
            self.data[country]=capital
        else:
            print('The country', country, 'is not included')
    def save_dict(self,filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
    @staticmethod
    def load_dict(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)


dict1=CountriesDict()
dict1.add_country("Slovakia","Bratislava")
dict1.add_country("USA","Washington, D.C.")
dict1.add_country("Czech republic","Prague")
dict1.add_country("Poland","Warszaw")
dict1.view_contents()
print('----------')
dict1.delete_country("Poland")
dict1.view_contents()
print('----------')
dict1.find_country("Slovakia")
print('----------')
dict1.edit_capital("Slovakia", 'Košice')
dict1.view_contents()
dict1.find_country("Slovakia")
print('----------')
dict1.save_dict("krajiny_mesta.txt")
loaded_dict=CountriesDict.load_dict("krajiny_mesta.txt")
loaded_dict.view_contents()





