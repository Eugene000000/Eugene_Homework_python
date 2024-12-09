class User:
    
    def __init__(self, firstname, lastname):
        print("создан")
        self.firstname = firstname
        self.lastname = lastname   

    def sayFirstName(self):
        print("меня зовут", self.firstname) 

    def sayLastName(self):
        print("моя фамилия", self.lastname)   

    def sayFullName(self):
        print("Полное имя", self.firstname, self.lastname)       

 