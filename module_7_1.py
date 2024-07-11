


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = "products.txt"

    def get_products(self):
        f = open(self.__file_name, 'r')
        all_products = f.read()
        f.close()
        return all_products

    def add(self, *products):
        f = open(self.__file_name, 'r+')
        all_products = [p.split()[0] for p in f]

        for i in products:
            if not i.name in all_products:
                f.write(f'{i.name} {i.weight} {i.category}\n')
                all_products.append(i.name)
            else:
                print(f'Продукт {i.name} уже есть в магазине')
        f.close()




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
