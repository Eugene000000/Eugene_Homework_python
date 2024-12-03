from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Apple" , "iphone 5S", "+79111111111")
phone2 = Smartphone("Nokia" , "3310", "+79222222222")
phone3 = Smartphone("Xiaomi" , "readme note 4", "+79333333333")
phone4 = Smartphone("Apple" , "iphone 10S", "+79444444444")
phone5 = Smartphone("Apple" , "iphone 15Pro", "+79555555555")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.number}")




