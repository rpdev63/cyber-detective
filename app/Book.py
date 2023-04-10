from datetime import date

class Book:
    def __init__(self, title: str, price: str, rating: int, availability: str, img_url: str) -> None:
        self.title = title
        self.price = price
        self.rating = rating
        self.availability = availability
        self.img_url = img_url
        self.id: int
        self.date: date

    def display_values(self):
        print(f"Titre : {self.title} - Prix : {self.price} - Note : {self.rating} - Disponibilité : {self.availability} - Lien Image : {self.img_url}")
