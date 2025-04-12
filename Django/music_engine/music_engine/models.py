from django.db import models

# Create your models here.

class Text_Choices():
    Genres = [
        ("Rap","RP", ),
        ("REGGAE", "R&B"),
        ("Hip-Hop","HP"),
        ("SAD","SD")
    ]
    GENDER =[
            ("MALE", "ML"),
            ("FEMALE", "FM"),
    ]


class Artist(models.Model):

    name = models.CharField(max_length=100)
    debut_year = models.DateField()
    gender = models.CharField(choices=Text_Choices.GENDER, default="--")
    age = models.PositiveIntegerField()
    genre = models.CharField(choices=Text_Choices.Genres, default="--")

    def __str__(self):
        return f"{self.name} : {self.age}"
    
class Genre(models.Model):
    genre = models.CharField(max_length=50, choices=Text_Choices.Genres, default="--")

    def __str__(self):
        return f"{self.genre}"