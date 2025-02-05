class Author:
    def __init__(self, name, location, contact, email, age):
        self.name = name
        self.location = location
        self.contact = contact
        self.email = email
        self.age = age

    def fetch_author(self):
        print(f"The author's name is {self.name}, of age {self.age}  the current location is {self.location},the email is{self.email},and her contact is{self.contact}.")
author_one = Author("Nawamwena", "Kayunga", "0706615389", "nawamwenaphicratte192@gmail.com", 22)  
author_one.fetch_author()
         