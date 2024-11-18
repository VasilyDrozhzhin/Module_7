import os


class Product:
	def __init__(self, name, weight, category):
		self.name = name
		self.weight = weight
		self.category = category

	def __str__(self):
		return f'{self.name}, {self.weight}, {self.category}'


class Shop:
	def __init__(self):
		self.__file_name = 'products.txt'

	def get_products(self):
		if not os.path.exists(self.__file_name):
			file = open(self.__file_name, 'w')
			file.close()
		else:
			file = open(self.__file_name, 'r')
			content = file.read()
			file.close()
			return content

	def add(self, *products):
		text = self.get_products()
		file = open(self.__file_name, 'a')
		for i in products:
			if i.name in text:
				print('Продукт ', str(i), ' уже есть в магазине')
			else:
				file.write(str(i) + '\n')
		file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
