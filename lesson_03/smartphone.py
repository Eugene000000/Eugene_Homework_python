class Smartphone:

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number   

    def phone(self):
        print(self.brand , self.model , self.number)

    def addPhone(self, catalog):
        self.newcatalog = catalog    

    def getPhone(self):
        return (self.phone)   